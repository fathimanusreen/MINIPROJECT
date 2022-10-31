from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import profileRgister
from user.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        formreg = profileRgister()
        if form.is_valid:
            form.save()
            user1 =User.objects.get(username=form.data['username']).id
            # print("sdf",user1)
            profile1 = Profile.objects.create(user_id=user1,customer=True)
            return redirect('user-login') #this is temparary redirect change it later
    else:
        form = UserCreationForm()
    context ={
        'form': form
    }
    return render(request,'user/register.html',context)


@login_required
def dashboard(request):
    if request.user.is_authenticated and Profile.objects.get(user=request.user).customer:
        return render(request,'customer/index.html')
    elif request.user.is_authenticated and Profile.objects.get(user=request.user).theatre:
        return render(request,'theatre/index.html')
    elif request.user.is_authenticated and Profile.objects.get(user=request.user).administrator:
        return render(request,'movieadministrator/index.html')