# Generated by Django 5.0.2 on 2024-02-24 19:17

import services.uploader
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='bashliq')),
                ('text', models.TextField(verbose_name='metn')),
                ('image', models.ImageField(blank=True, null=True, upload_to=services.uploader.Uploader.upload_photo_about)),
                ('questions', models.CharField(max_length=255, verbose_name='verilen suallar')),
                ('answers', models.CharField(max_length=255, verbose_name='cavblar')),
                ('info', models.TextField(verbose_name='haqqimizda melumatlar')),
            ],
            options={
                'verbose_name': 'haqqimizda',
                'verbose_name_plural': 'haqqimizdakilar',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='bashliq')),
                ('text', models.TextField(verbose_name='metn')),
                ('image', models.ImageField(blank=True, null=True, upload_to=services.uploader.Uploader.upload_photo_blog)),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'bloglar',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='ad ve soyad')),
                ('email', models.CharField(max_length=255, verbose_name='email adress')),
                ('subject', models.CharField(max_length=255, verbose_name='movzu')),
                ('mesage', models.TextField(verbose_name='mesaj')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contactlar',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MainDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('adresss', models.CharField(max_length=255, verbose_name='adress')),
                ('phones', models.CharField(max_length=255, verbose_name='phones')),
                ('locations', models.TextField(blank=True, null=True, verbose_name='locations')),
                ('name', models.CharField(max_length=255, verbose_name='adi')),
                ('voen', models.CharField(max_length=255, verbose_name='voen nomresi')),
                ('voen_adress', models.CharField(max_length=255, verbose_name='voen unvani')),
            ],
            options={
                'verbose_name': 'elaqe melumati',
                'verbose_name_plural': 'elaqe melumatlari',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='SosialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sosial_name', models.CharField(choices=[('insta', 'Instagram'), ('fb', 'Facebook'), ('wp', 'WhatsApp'), ('twitter', 'Twitter'), ('linkedin', 'Linkedin'), ('tiktok', 'Tiktok')], max_length=255, verbose_name='sosial media hesabi')),
                ('sosial_link', models.TextField(verbose_name='sosial media linki')),
            ],
            options={
                'verbose_name': 'sosial media hesabi',
                'verbose_name_plural': 'sosial media hesablari',
                'ordering': ('sosial_name',),
            },
        ),
    ]