# Generated by Django 4.1.2 on 2022-11-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0005_delete_uploadfilesin'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadfilemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
