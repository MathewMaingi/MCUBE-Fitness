
from django.contrib import admin
from django.urls import path
from GYM import views
from GYM.views import update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('classes/', views.classes, name='classes'),
    path('contact/', views.contact, name='contact'),
    path('elements/', views.elements, name='elements'),
    path('login/', views.login, name='login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('registration/', views.registration, name='registration'),

    path('inner/', views.inner, name='inner'),
    path('trainer/', views.add_trainer, name='trainer'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('add_recent_post/', views.add_recent_post, name='add_recent_post'),
    path('gallery/', views.gallery, name='gallery'),
    path('pay/', views.pay, name='pay'),

    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>/', update, name='update'),
    path('update/<str:model_name>/<int:id>/', update, name='update'),

    path('manage/', views.manage, name='manage'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_class/', views.add_class, name='add_class')
]
