# Generated by Django 4.1.2 on 2022-10-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=100, verbose_name='Должность')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Фамилия')),
                ('alt_name', models.CharField(blank=True, max_length=30, verbose_name='Отчество')),
                ('experience', models.TextField(blank=True, verbose_name='Опыт работы')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('birthday', models.DateField(blank=True, verbose_name='Дата рождения')),
                ('phone_number', models.CharField(blank=True, max_length=50, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
    ]