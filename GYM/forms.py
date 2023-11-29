from django import forms
from GYM.models import Trainer, Blog, ImageModel, Subscription, ClassModel, RecentPost


class Traineruploadform(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['image', 'name', 'speciality', 'specialitydescription']


class Bloguploadform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image', 'about', 'description']

class RecentPostUploadForm(forms.ModelForm):
    class Meta:
        model = RecentPost
        fields = ['image', 'about', 'description', 'date']


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'stock', 'price']

class ClassUploadForm(forms.ModelForm):
    class Meta:
        model = ClassModel
        fields = ['classimage', 'classname', 'classdetails']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['subscribeemail']