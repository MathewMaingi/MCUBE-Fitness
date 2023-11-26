from django import forms
from GYM.models import Trainer, Blog


class Traineruploadform(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['image', 'name', 'speciality']


class Bloguploadform(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['tab_name', 'blogimage', 'about', 'description']
