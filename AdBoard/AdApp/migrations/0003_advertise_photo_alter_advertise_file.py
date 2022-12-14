# Generated by Django 4.1.3 on 2022-11-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdApp', '0002_alter_reply_advertise'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='advertise',
            name='file',
            field=models.FileField(blank=True, upload_to='AdApp_files/', verbose_name='File'),
        ),
    ]
