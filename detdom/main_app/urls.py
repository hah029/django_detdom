from django.urls import path
from . import views


app_name = 'detdom'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('children/', views.childrenPage, name='children'),
    path('teachers/', views.teachersPage, name='teachers'),
    path('admins/', views.administrationPage, name='admins'),
    path('gallery/', views.galleryPage, name='gallery'),
    path('about/', views.aboutPage, name='about')
]
