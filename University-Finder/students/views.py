
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import *
from .forms import *
from .filter import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django import forms

import re


@login_required(login_url='login')
def home(request):
    user = User.objects.all()
    university = University.objects.all()

    

    total_users = user.count()
    total_university = university.count()
    context = {
        'total_users': total_users,
        'total_university': total_university,
    }
    return render(request, 'students/home.html', context)

def landing_page(request):  

    context = {}

    return render(request, 'students/index.html', context)

@unauthenticated_user
def registerPage(request):

    username_regex = '^(?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$'
    

    # Only contains alphanumeric characters, underscore and dot.
    # Underscore and dot can't be at the end or start of a username (e.g _username / username_ / .username / username.).
    # Underscore and dot can't be next to each other (e.g user_.name).
    # Underscore or dot can't be used multiple times in a row (e.g user__name / user..name).
    # Number of characters must be between 8 to 20.


    if request.method == "POST":
        fname = request.POST.get('fname')
        sname = request.POST.get('sname')
        usern = request.POST.get('username')
        password1 = request.POST.get('one_p')
        password2 = request.POST.get('second_p')
        date = request.POST['date']
        month = request.POST['month']
        year = request.POST['year']
        gen = request.POST['gender']

        if(not re.search(username_regex, usern)):
            messages.error(request, "Please choose a decent username.")
            return redirect('register')

        if(len(fname) == 0 or len(sname) == 0):
            messages.error(request, "Found some empty fields. Please fill it.")
        
        if(password1 != password2):
            messages.error(request, "Re-entered password do not match.")
            return redirect('register')

        user = User.objects.create_user(
            first_name = fname,
            last_name = sname,
            username = usern,
            password = password1,
        )
        user.save()            


        st = Student(
            student_id = usern,
            password = password1,
            first_name = fname,
            last_name = sname,
            gender = gen,
        )
        st.save()

        messages.success(request, "Account was created for " + usern + ".")
        return redirect('login')

    context = {}
    return render(request, 'students/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Error : Username or Password is incorrect.")

    context = {}
    return render(request, 'students/login.html', context)

def donatePay(request):
    context = {}

    if request.method == "POST":
        amount = request.POST.get('amount')

        if amount == "":
            messages.error(request, "Input field empty. Please enter something.")
            return redirect('donate_pay')

        response = redirect('donate')
        response.set_cookie('amount', amount)
        return response
        
    return render(request, 'students/donate-pay.html', context)

    
    

def donate(request):
    amount = request.COOKIES['amount']
    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    context = {
        'amount': amount,
    }

    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        street = request.POST.get('street')
        zip_code = request.POST.get('zip_code')
        city = request.POST.get('city_name')
        country = request.POST['country_name']
        card_no = request.POST.get('card_number')
        date = request.POST['date']
        month = request.POST['month']
        CVV = request.POST.get('CVV')

        if(not re.search(regex_email, email)):
            messages.error(request, "Please enter correct Email Address.")
            return redirect('donate')
        
        if(len(first_name) == 0 or len(last_name) == 0 or len(street) == 0 or len(city) == 0):
            messages.error(request, "Found some empty fields. Please fill it.")
            return redirect('donate')

        if( len(str(zip_code)) != 6) :
            messages.error(request, "Please enter the correct Zip Code. Number of digits do not match.")
            return redirect('donate')

        if( len(str(card_no)) < 13 and len(str(card_no)) > 19):
            messages.error(request, "Please enter the correct Card Number. Number of digits do not match.")
            return redirect('donate')
        
        if( len(str(CVV)) < 3 and len(str(CVV)) > 4 ):
            messages.error(request, "Please enter correct CVV.")
            return redirect('donate')

        
        don_inf = DonationInfo(
            email = email,
            first_name = first_name,
            last_name = last_name, 
            street = street,
            zip_code = int(zip_code),
            city = city,
            country = country,
        )
        don_inf.save()

        return redirect('landing_page')


    return render(request, 'students/donate.html', context)

@login_required(login_url='login')
def logoutUser(request):

    if request.method == "POST":
        logout(request)
        return redirect('landing_page')

    return render(request, 'students/logout_page.html')

@login_required(login_url='login')
def deleteUser(request):
    user = request.COOKIES['username']    
    name = request.user.get_full_name()
        

    context = {
        "user": user,
        "name": name,
    }

    if request.method == "POST":
        u = User.objects.get(username = user)
        logout(request)
        u.delete()
        return redirect('landing_page')

    return render(request, 'students/del_acc.html', context)

@login_required(login_url='login')
def userDetail(request, usrn):
    detail = Student.objects.get(student_id=usrn)
    form = DetailsForm(instance=detail)
    print(form)

    if request.method == "POST":
        if request.POST.get('para') == "data_update":
            form = DetailsForm(request.POST, instance=detail)
            if form.is_valid():
                firstName = form.cleaned_data.get('first_name')
                lastName = form.cleaned_data.get('last_name')
                Email = form.cleaned_data.get('email')
                st_id = form.cleaned_data.get('student_id')
                lvl = form.cleaned_data.get('level')
                deg = form.cleaned_data.get('degree_name')

                Student.objects.filter(student_id=usrn).update(
                    first_name=firstName, last_name=lastName, email=Email, student_id=st_id, level=lvl, degree_name=deg)

                return redirect('home')
        
        elif request.POST.get('para') == "delete-acc":
            request = redirect('delete_user')
            request.set_cookie('username', usrn)
            return request

    

    context = {'form': form}
    return render(request, 'students/user-detail.html', context)

@login_required(login_url='login')
def finderPage(request):

    university = University.objects.all()

    myFilter = UniversityFilter(request.GET, queryset=university)
    univ = myFilter.qs
    print(myFilter.form)
    context = {
        'univ': univ,
        'myFilter': myFilter,
    }
    return render(request, 'students/finder.html', context)


@login_required(login_url='login')
def univDetailPage(request):

    univ = University_Info.objects.all()

    myFil = universityInfoFilter(request.GET, queryset=univ)
    u = myFil.qs
    m = u.first()

    print(m)
    print(myFil)
    print(myFil.form)

    context = {
        'u': u,
        'myFil': myFil,
        'm': m,
    }

    return render(request, 'students/univ_info.html', context)

