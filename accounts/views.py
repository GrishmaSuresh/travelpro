from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        username = str(request.POST.get('username'))
        firstname = str(request.POST.get('firstname'))
        lastname = str(request.POST.get('lastname'))
        email = str(request.POST.get('email'))
        password = str(request.POST.get('password'))

        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
            return redirect('/accounts/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists')
            return redirect('/accounts/register')
        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                            password=password, email=email)
            user.save()
            print("user created")
            return redirect('/accounts/login')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = str(request.POST.get('username'))
        password = str(request.POST.get('password'))

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('/accounts/login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
