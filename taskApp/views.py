from django.shortcuts import render
from taskApp.forms import UserForm,UserCustomForm,UserTaskForm
from taskApp.models import UserCustom,UserTask
#below libraries required for login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'taskApp/index.html')

@login_required
def toggle(request):
    task_obj=UserTask.objects.filter(author=request.user)
    if request.method=='POST':
        val=request.POST.get('status',None)
        t = UserTask.objects.get(id=val)
        t.status = True
        t.save()
    return render(request,'taskApp/task.html',{'task_obj':task_obj})

@login_required
def add_task(request):
    added=False

    if request.method == "POST":
        task_form=UserTaskForm(data=request.POST)

        if task_form.is_valid():
            task=task_form.save(commit=False)
            #print("NAME:"+str(request.user))
            task.author=request.user
            task.save()
            added=True

        else:
            print(task_form.errors)


    else: #no request=POST yet
        task_form=UserTaskForm()

    return render(request,'taskApp/addTask.html',{'added':added,'task_form':task_form})

@login_required
def my_task(request):
    task_obj=UserTask.objects.filter(author=request.user)
    return render(request,'taskApp/task.html',{'task_obj':task_obj,'user_key':request.user})


@login_required
def user_logout(request):  #only login users can logout
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered=False

    if request.method == "POST":

        user_form=UserCustomForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    else: #no request=POST yet
        user_form=UserCustomForm()
        profile_form=UserProfileInfoForm()

    return render(request,'taskApp/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered })



def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')  #name of element
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('taskApp:myTask')) #myTask is the name of url , go to urls.py
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supllied!")

    else:
        return render(request,'taskApp/login.html',{})
