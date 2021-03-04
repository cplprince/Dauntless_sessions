from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class loginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(
          widget = forms.PasswordInput(
              attrs = {
                "class" : "form-control",
                "id": "user-password"
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
      
      