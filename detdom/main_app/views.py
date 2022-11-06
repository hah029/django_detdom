# from django.http import HttpResponse
# import datetime
from django.shortcuts import render

from . import models


def homePage(request):
    context = {
        'header': 'Главная страница'
    }
    return render(request, 'detdom/home.html', context=context)


def childrenPage(request):
    context = {
        'header': 'Наши дети'
    }
    return render(request, 'detdom/children.html', context=context)


def teachersPage(request):
    teachers = models.Teacher.objects.all()
    context = {
        'header': 'Преподаватели',
        'teachers': teachers,
    }
    return render(request, 'detdom/teachers.html', context=context)


def administrationPage(request):
    teachers = models.Teacher.objects.all()
    context = {
        'header': 'Администрация',
        'teachers': teachers,
    }
    return render(request, 'detdom/administration.html', context=context)


def aboutPage(request):
    context = {
        'header': 'О нас'
    }
    return render(request, 'detdom/about.html', context=context)


def galleryPage(request):
    context = {
        'header': 'Галерея'
    }
    return render(request, 'detdom/gallery.html', context=context)
