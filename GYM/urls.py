
from django.contrib import admin
from django.urls import path
from GYM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('classes/', views.classes, name='classes'),
    path('contact/', views.contact, name='contact'),
    path('elements/', views.elements, name='elements'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('inner/', views.inner, name='inner'),
    path('trainer/', views.add_trainer, name='trainer'),
    path('add_blog/', views.add_blog, name='add_blog')
]
