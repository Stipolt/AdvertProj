# Generated by Django 4.1.3 on 2022-11-24 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('time_pub', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, upload_to='AdApp_files/', verbose_name='Файл')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('msg', models.TextField(max_length=200)),
                ('advertise', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AdApp.advertise', verbose_name='Объявление')),
            ],
        ),
        migrations.AddField(
            model_name='advertise',
            name='category',
            field=models.ManyToManyField(through='AdApp.AdCat', to='AdApp.category'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='adcat',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdApp.advertise'),
        ),
        migrations.AddField(
            model_name='adcat',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdApp.category'),
        ),
    ]
