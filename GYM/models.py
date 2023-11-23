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

