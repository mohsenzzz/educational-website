from django.http import HttpResponse
from django.shortcuts import render, redirect
from redis import Redis
from services.messageBroker import push_value,pop_value
from user.forms import UserForm


# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')

    if request.method == 'POST':
        print(request.POST['username'],request.POST['phone_number'])
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            phone_number = request.POST['phone_number']
            push_value('phone',phone_number)
            # user_form.save()
            request.session['phonenumber'] = phone_number
            return redirect('login')
        return render(request, 'user/register.html', {'userform': user_form})

def login(request):

    if request.method == 'GET':
        # print(request.session['phonenumber'],'login')
        return render(request, 'user/login.html')
    if request.method == 'POST':
        code = pop_value(request.session['phonenumber'])
        code = code[1].decode('utf-8')
        user_code = request.POST['code']
        print('code',code)

        print(code)
        if user_code == code:
            print('here')
            return redirect('profile')
        else:
            return render(request, 'user/login.html', {'error_message':'this code is not true'})

def get_profile(request):
    if request.method == 'GET':
        return render(request, 'user/profile.html')