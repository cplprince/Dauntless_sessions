from django.shortcuts import render,redirect

from .forms import loginForm,registerForm

from django.contrib.auth import authenticate, login, logout, get_user_model
User = get_user_model()

# Create your views here.

def login_view(request):
  form = loginForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password")
    
    user = authenticate(request, username=username,password=password) #None
  
    if user != None:
      #is_active , user is banned, 
      #request.user == user
      login(request, user)
      return redirect("/home")
    else:
      #attemp = request.session.get("attempt") or 0
      #request.session["attempt] = attempt + 1
      #return redirect("/invalid-password")
      request.session["invalid-user"] = 1 #1==True
  return render(request, "forms.html", {"form":form})
  
def logout_view(request):
    logout(request)
    #request.user == Anon user
    return redirect("/login")
  
  
def register_view(request):
  form = registerForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get("username")
    email = form.cleaned_data.get("email")
    password = form.cleaned_data.get("password1")
    password2 = form.cleaned_data.get("password2")
    
    print(username,email,password,password2)
    user = User.objects.create_user(username,email,password)
    
    if user != None:
      login(request, user)
      return redirect("/")
    else:
      request.session["register_error"] = 1
      
  return render(request, "forms.html",{"form":form})