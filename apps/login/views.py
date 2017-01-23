from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import User
from..books.models import Review

def form(request):
    return render(request, 'login/form.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        response = User.objects.login(email=email, password=password)

        if 'login_errors' in response:
            messages.error(request, response['login_errors'], extra_tags='login_error')
        elif 'success' in response:
            request.session['user'] = response['success']
            messages.success(request, 'You have been logged in')
            return redirect('books:index')

    return redirect('login:form')

def register(request):
    if request.method == 'POST':
        response = User.objects.register(request.POST)
        if 'registration_errors' in response:
            for error in response['registration_errors']:
                messages.error(request, error, extra_tags='register_error')
        elif 'success' in response:
            request.session['user'] = response['success']
            messages.success(request, 'Welcome to the club, {}!'.format(response['success']['name']))
            return redirect('books:index')
    return redirect('login:form')

def logout(request):
    request.session.clear()
    return redirect('login:login')

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    reviews = Review.objects.filter(user=user)
    return render(request, 'login/profile.html', {'user': user, 'reviews':reviews})
