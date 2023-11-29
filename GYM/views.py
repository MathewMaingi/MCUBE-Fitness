import json


from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect



from GYM.models import Member, Contact, ImageModel, Subscription, ClassModel

from GYM.forms import Traineruploadform, ImageUploadForm, SubscriptionForm, ClassUploadForm, Bloguploadform, \
    RecentPostUploadForm
from GYM.models import Trainer, Blog, RecentPost, Subscription


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
    classes = ClassModel.objects.all()
    return render(request, 'classes.html', {'classes': classes})


def elements(request):
    return render(request, 'elements.html')


def login(request):
    return render(request, 'login.html')


def admin_login(request):
    return render(request, 'managerlogin.html')


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


def subscribe(request):
    if request.method == 'POST':
        Subscriber = SubscriptionForm(subscribeemail=request.POST['email'], )
        Subscriber.save()
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



def add_recent_post(request):
    if request.method == 'POST':
        form = RecentPostUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/add_recent_post')
    else:
        form = RecentPostUploadForm()
    return render(request, 'add_recent_post.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/add_product')
    else:
        form = ImageUploadForm()
    return render(request, 'add_product.html', {'form': form})


def add_class(request):
    if request.method == 'POST':
        form = ClassUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/add_class')
    else:
        form = ClassUploadForm()
    return render(request, 'add_class.html', {'form': form})


def gallery(request):
    images = ImageModel.objects.all()
    return render(request, 'gallery.html', {'images': images})

def blog(request):
    blogs = Blog.objects.all()
    post = RecentPost.objects.all()
    return render(request, 'blog.html', {'blogs': blogs, 'post' : post})



def pay(request):
    return render(request, 'pay.html')


def manage(request):
    images = ImageModel.objects.all()
    trainer = Trainer.objects.all()
    subscriptions = Subscription.objects.all()
    classes = ClassModel.objects.all()



    return render(request, 'admin.html',{'trainer': trainer, 'images': images, 'subscriptions': subscriptions, 'classes': classes})


"""def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/image')"""


def update(request, id):
    images = ImageModel.objects.get(id=id)
    form = ImageUploadForm(request.POST, instance=images)
    trainer = Trainer.objects.get(id=id)
    form = Traineruploadform(request.POST, instance=trainer)
    subscriptions = Subscription.objects.get(id=id)

    classes = ClassModel.objects.get(id=id)
    form = ClassUploadForm(request.POST, instance=classes)

    if form.is_valid():
        form.save()
        return redirect('/update')
    else:
        return render(request, 'adminedit.html',
                      {'trainer': trainer, 'images': images, 'subscriptions': subscriptions, 'classes': classes})


def delete(request, id):
    images = ImageModel.objects.get(id=id)
    trainer = Trainer.objects.get(id=id)
    subscriptions = Subscription.objects.get(id=id)
    classes = ClassModel.objects.get(id=id)
    images.delete()
    trainer.delete()
    subscriptions.delete()
    classes.delete()
    return redirect('/admin')


def edit(request, id):
    images = ImageModel.objects.get(id=id)
    trainer = Trainer.objects.get(id=id)
    subscriptions = Subscription.objects.get(id=id)
    classes = ClassModel.objects.get(id=id)
    return render(request, 'adminedit.html',
                  {'trainer': trainer, 'images': images, 'subscriptions': subscriptions, 'classes': classes})
