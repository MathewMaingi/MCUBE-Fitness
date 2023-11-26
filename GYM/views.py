from django.shortcuts import render, redirect
from GYM.models import Member, Contact

from GYM.forms import Traineruploadform, Bloguploadform
from GYM.models import Trainer, Blog


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
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def add_trainer(request):
    if request.method == 'POST':
        form = Traineruploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/trainer')
    else:
        form = Traineruploadform()
    return render(request, 'add_trainer.html', {'form': form})


def about(request):
    trainer = Trainer.objects.all()
    return render(request, 'about.html', {'trainer': trainer})


def add_blog(request):
    if request.method == 'POST':
        form = Bloguploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/add_blog')
    else:
        form = Bloguploadform()
    return render(request, 'add_blog.html', {'form': form})


def blog(request):
    categories = [
        ('events and competitions', 'nutrition tips'),
        ('body building', 'pilates and yoga'),
        ('workout', 'fitness'),
        ('wellness treatments', 'uncategorized'),
    ]  # Add more categories as needed
    blogimage = {category: Blog.objects.filter(tab_name=category) for category in categories}
    return render(request, 'blog.html', {'categories': categories, 'Blog': Blog})



