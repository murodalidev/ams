# Generated by Django 3.2.5 on 2021-08-23 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('image', models.FileField(upload_to='service/icon/', verbose_name='Image')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Advantage',
                'verbose_name_plural': 'Advantages',
            },
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('count', models.IntegerField(verbose_name='Counter')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Counter',
                'verbose_name_plural': 'Counters',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('image', models.FileField(upload_to='service/icon/', verbose_name='Image')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('full_name', models.CharField(max_length=100, verbose_name='Full name')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone number')),
                ('type_of_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.service', verbose_name='Service')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
