# Generated by Django 2.2.10 on 2021-07-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trapsi', '0003_client_enquire'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('mobileno', models.CharField(max_length=180)),
                ('email', models.CharField(max_length=180)),
                ('company', models.CharField(max_length=180)),
                ('date', models.DateField(auto_now_add=True)),
                ('phone', models.CharField(max_length=140)),
                ('intrest', models.TextField()),
                ('subject', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='registrationapplication',
            name='city',
        ),
        migrations.AddField(
            model_name='registrationapplication',
            name='email',
            field=models.CharField(default=11, max_length=180),
            preserve_default=False,
        ),
    ]
