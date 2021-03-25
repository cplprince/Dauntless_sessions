from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

not_allowed_username = ["abc","admin","support"]

class loginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(
          widget = forms.PasswordInput(
              attrs = {
                "id": "user-password",
                "class" : "form-control",
              }
          )
  )

  #def clean(self):
  #  username = self.cleaned_data.get("username")
  #  password = self.cleaned_data.get("password")


  def clean_user(self):
    username = self.cleaned_data.get("username")
    qs = user.objects.filter(username__iexact=username) # ""ThisIsMyNAME" ==> "thisismyname""
    if not qs.exist():
      raise forms.ValidationsError("This is an invalid username.")
    return username


class registerForm(forms.Form):
  username = forms.CharField()
  email = forms.CharField()
  password1 = forms.CharField(
    label = "password",
    widget = forms.PasswordInput(
      attrs = {
        "class" : "form-control",
        "id": "user-password"
      }
    )
  )
  password2 = forms.CharField(
    label = "confirm password",
    widget = forms.PasswordInput(
      attrs = {
        "class" : "form-control",
        "id": "user-confirm-password"
      }
    )
  )

  def clean_username(self):
    username = self.cleaned_data.get("username")
    qs = User.objects.filter(username__iexact = username) #NULL
    if username in not_allowed_username:
      raise forms.ValidationsError("This is an invalid username")
    if qs.exists():
      raise forms.ValidationsError("This is an invalid username")
    return username

  def clean_email(self):
    email = self.cleaned_data.get("email")
    qs = User.objects.filter(email__iexact = email) #null {"email":"xxx@email.com"}
    if qs.exists(): #True == NUll #False == {}
      raise forms.ValidationsError("This email is already in use")
    return email
