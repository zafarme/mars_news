from django.shortcuts import render,redirect

from .forms import LoginForm,RegistrationForm
from .models import User,UserProfile,New

from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required


def main_page(request):
    news = New.objects.all()
    return  render(request, 'index.html',context={'news':news})






def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)


        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username,password)

            if user:
                login(request,user)

                return redirect('/')
            
    else:
        form = LoginForm()

        
    return render(request, 'login.html', context={'form': form})





