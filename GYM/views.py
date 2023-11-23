from django.shortcuts import render, redirect
from GYM.models import Member, Contact


# Create your views here.
def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def classes(request):
    return render(request, 'classes.html')


def elements(request):
    return render(request, 'elements.html')


def login(request):
    return render(request, 'login.html')

def inner(request):
    return render(request, 'inner-page.html')


def registration(request):
    if request.method == 'POST':
        members = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                         password=request.POST['password'], phonenumber=request.POST['phonenumber'],
                         email=request.POST['email'], birthdate=request.POST['birthdate'],
                         gender=request.POST['gender'], username=request.POST['username'])
        members.save()
        return redirect('/')
    else:
        return render(request, 'registration.html')


def contact(request):
    if request.method == 'POST':
        contacts = Contact(contactname=request.POST['contactname'], email=request.POST['email'],
                           subject=request.POST['subject'], message=request.POST['message'])
        contacts.save()
        return redirect('/home')
    else:
        return render(request, 'contact.html')
