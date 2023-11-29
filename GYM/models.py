from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=40,default='fname')
    lastname = models.CharField(max_length=40,default='lname')
    password = models.CharField(max_length=10,default='xxx')
    phonenumber = models.IntegerField(default='1234567890')
    email = models.EmailField(default='contact@gmail.com')
    birthdate = models.DateField(default=1234)
    gender = models.CharField(max_length=15,default='gender')
    username=models.CharField(max_length=20,default='Username')



    def __str__(self):
        return self.firstname+""+self.lastname



class Contact(models.Model):
    contactname = models.CharField(max_length=30,default='name')
    email = models.EmailField(default='contact@gmail.com')
    subject = models.CharField(max_length=100,default='subject')
    message = models.CharField(max_length=500,default='message')

    def __str__(self):
        return self.contactname

class Trainer(models.Model):
    image = models.ImageField(upload_to='my-trainers/', default='default.png')
    name = models.CharField(max_length=50, default='name')
    speciality = models.CharField(max_length=500, default='Mcube')
    specialitydescription = models.TextField(default='Speciality')
    trainerpassword = models.CharField(max_length=30,default='12345')



    def __str__(self):
        return self.name



class Blog(models.Model):
    image = models.ImageField()
    about = models.CharField(max_length=100, default='about')
    description = models.TextField(default='describe')
    def __str__(self):
        return  self.about

class RecentPost(models.Model):
    image = models.ImageField()
    about = models.CharField(max_length=100)
    description = models.TextField(default='describe')
    date = models.DateField()

    def __str__(self):
        return  self.about


class ImageModel(models.Model):
    image = models.ImageField(upload_to='(gallery/')
    title = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class ClassModel(models.Model):
    classimage = models.ImageField(upload_to='(gallery/')
    classname = models.CharField(max_length=50)
    classdetails = models.TextField()


    def __str__(self):
        return self.classname

class Subscription(models.Model):
    subscribeemail = models.EmailField(unique=True, default="mathewmaingi21@gmail.com")

    def __str__(self):
        return self.subscribeemail