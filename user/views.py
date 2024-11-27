from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from phonenumber_field.phonenumber import PhoneNumber,phonenumbers
from django.contrib.auth import login as auth_login,authenticate
from services.messageBroker import push_value,pop_value
from phonenumber_field.modelfields import PhoneNumberField
from user.forms import UserForm,LoginForm, UpdateForm
from user.models import User


# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        number = PhoneNumberField(request.POST['phone_number'],region='IR')

        if user_form.is_valid():
            phone_number = request.POST['phone_number']
            push_value('phone', phone_number)
            user_form.save()

            request.session['phonenumber'] = request.POST['phone_number']
            return redirect('verify_user')
        return render(request, 'user/register.html', {'userform': user_form})

def login(request):
    '''
    this method is used to register the user by phone_number
    :param request:
    :return:
    '''

    if request.method == 'GET':
        return render(request, 'user/login.html')

    if request.method == 'POST':

        login_form = LoginForm(request.POST)

        if login_form.is_valid():
           username = login_form.cleaned_data['username']
           password = login_form.cleaned_data['password']

           user = authenticate(request,username=username, password=password)
           if user is not None:
               auth_login(request, user)

               # return render(request, 'user/profile.html',{'user':user})
               return redirect('profile')
        return render(request, 'user/login.html', {'login_form': LoginForm(),'message':'username or password is incorrect'})

def verify_user(request):

    if request.method == 'GET':
        return render(request, 'user/verify.html')

    if request.method == 'POST':
        #get verify code from redis and check to entered code by user
        code = pop_value(request.session['phonenumber'])
        code = code[1].decode('utf-8')
        user_code = request.POST['code']

        if user_code == code:
            phone_number =PhoneNumber.from_string(request.session['phonenumber'],region='IR')
            user = User.objects.filter(phone_number=phone_number).first()
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return render(request, 'user/verify.html', {'error_message':'this code is not true'})

# def get_verify_profile(request):
#     if request.method == 'GET':
#             phone_number = PhoneNumber.from_string(request.session['phonenumber'],region='IR')
#             user = User.objects.filter(phone_number=phone_number).first()
#             if user.is_active:
#                 return render(request, 'user/profile.html', {'user': user})
#             else:
#                 return render(request, 'user/forbidden.html', {'error_message':'this user is not active'})


def get_profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            # phone_number = str(request.user.phone_number)
            # request.user.phone_number=phonenumbers.parse(phone_number).national_number
            return render(request, 'user/profile.html', {'user': request.user})
        else:
            return render(request, 'user/forbidden.html', {'error_message': 'you are not logged in'})

@login_required
def edit_profile(request,pk):
    if request.method == 'POST':

        user = User.objects.filter(pk=pk).first()

        form = UpdateForm(request.POST)
        print(form.is_valid())
        if form.is_valid():

            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.username = request.POST['username']
            user.save()
            return redirect('profile')
            # return render(request, 'user/profile.html', {'user_form': form, 'user': user})
        return render(request, 'user/profile.html', {'user_form': UpdateForm()})