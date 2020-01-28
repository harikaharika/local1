from django.shortcuts import render,redirect
from django.contrib.auth.models import User ,auth
# Create your views here.



def login(request):
    if request.method=='POST':
        username = request.POST.get('user_name')
        password1 = request.POST.get('password1')

        user = auth.authenticate(username=username,password=password1)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('user_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        print('user created')
        return redirect('/')

    else:
        return render(request,'register.html')