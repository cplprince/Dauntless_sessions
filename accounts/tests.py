from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class user_test_case(TestCase):

    def setUp(self):
        user_a = User(username="plm",email="mail@mail.com")
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password("12345")
        user_a.save()
        #User.objects.create()
        #User.objects.create_user()
        print(user_a.id)
        self.user_a = user_a


    def test_user_exist(self):
        user_count = User.objects.all().count()
        print(user_count)
        self.assertEqual(user_count,1)
        self.assertNotEqual(user_count,0)

    def test_user_password(self):
        self.assertTrue(
            self.user_a.check_password("12345")
            )

    def test_login_url(self):
        #LOGIN_URL ="/login"
        #self.assertEqual(settings.LOGIN_URL, LOGIN_URL)
        login_url = settings.LOGIN_URL
        #self.client.get , self.client.post
        #response = self.client.post(url, {"data"} , follow=True)
        data = {"username":"plm","password":"12345"}
        response = self.client.post(login_url, data, follow=True)
        #print(dir(response))
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(status_code, 200)
        self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
