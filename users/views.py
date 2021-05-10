from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard-home')
    if request.method == "POST":
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard-home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid User Credentials!'})
    else:
        return render(request, 'users/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard-home')
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'users/register.html', {'error' : "Username already exists"})
            except User.DoesNotExist:
                if (request.POST['email'].find('@thapar.edu') == -1):
                    return render(request, 'users/register.html', {'error' : "Please give your university email address"})
                if (len(str(request.POST['rollno'])) != 9) or str(request.POST['rollno'])[:2] != "10":
                    return render(request, 'users/register.html', {'error' : "Invalid roll no."})
                try:
                    profile = Profile.objects.get(rollno = request.POST['rollno'])
                    return render(request, 'users/register.html', {'error' : "An account for this rollno already exists ! "})
                except Profile.DoesNotExist:
                    user = User.objects.create_user(username = request.POST['username'], email = request.POST['email'], password = request.POST['password1'], first_name = request.POST['first_name'], last_name = request.POST['last_name'])
                    profile = Profile(rollno = request.POST['rollno'], dob = request.POST['dob'], block = request.POST['block'], roomno = request.POST['roomno'], phone = request.POST['phone'], user = user)
                    profile.save()
                    auth.login(request, user)
                    return redirect('dashboard-home')
        else:
            return render(request, 'users/register.html', {'error' : "Passwords do not match"})
    return render(request, 'users/register.html')


