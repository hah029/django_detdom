from django.db import models

# Create your models here.
class Teacher(models.Model):

    job_title = models.CharField(max_length=100, blank=True, verbose_name='Должность')

    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    alt_name = models.CharField(max_length=30, blank=True, verbose_name='Отчество')

    experience = models.TextField(blank=True, verbose_name='Опыт работы')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")

    birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True, verbose_name="Дата рождения")

    phone_number = models.CharField(max_length=50, blank=True, verbose_name='Номер телефона')

    group = models.CharField(max_length=50, blank=True, verbose_name='Группа')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.alt_name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'