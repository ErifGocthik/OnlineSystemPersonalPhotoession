# Generated by Django 5.0.3 on 2024-03-26 08:24

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256, verbose_name='Электронная почта')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('phone_number', models.CharField(blank=True, max_length=32, null=True, validators=[django.core.validators.RegexValidator('/^\\+?(\\d{1,3})?[- .]?\\(?(?:\\d{2,3})\\)?[- .]?\\d{3}?\\d{3}$/')])),
                ('photosession_type', models.CharField(choices=[('1', 'Портрет.'), ('2', 'Фотоссестия Пары (Love Story).'), ('3', 'Репортаж.'), ('4', 'Fashion.'), ('5', 'Предметная Фотография.'), ('6', 'Пейзаж.'), ('7', 'Архитектурная Фотография.'), ('8', 'Стиль "ню".'), ('9', 'Фотографии детей.'), ('10', 'Съёмка домашних животных или диких животных.'), ('11', 'Свадебная фотосессия.'), ('12', 'Фотосъёмка беременных.'), ('13', 'Макросъёмка.')], default='1', max_length=64, verbose_name='Тип фотосессии')),
                ('example', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Примеры')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=256, unique=True, verbose_name='Имя Пользователя')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='Электронная почта')),
                ('name', models.CharField(max_length=256, verbose_name='Имя')),
                ('surname', models.CharField(max_length=256, verbose_name='Фамилия')),
                ('password', models.CharField(max_length=256, validators=[django.core.validators.MinLengthValidator(8, 'Пароль должен быть не меньше 8 символов'), django.core.validators.MaxLengthValidator(256, 'Пароль должен быть не более 256 символов')])),
                ('user_type', models.CharField(choices=[('1', 'Клиент'), ('2', 'Фотограф')], default='1', max_length=64, verbose_name='Тип Пользователя')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='default/default_profile_image.png', null=True, upload_to='%Y/%m/%d/', verbose_name='Фотография')),
                ('bio', models.TextField(blank=True, default='Задача организации, в особенности же перспективное планирование не даёт нам иного выбора, кроме определения переосмысления внешнеэкономических политик. Для современного мира синтетическое тестирование выявляет срочную потребность инновационных методов управления процессами. Являясь всего лишь частью общей картины, ключевые особенности структуры проекта набирают популярность среди определенных слоев населения, а значит, должны быть в равной степени предоставлены сами себе.', null=True, verbose_name='Биография')),
                ('tech', models.CharField(blank=True, default='Без Зеркальная камера EOS R5', max_length=256, null=True, verbose_name='Техника')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.TextField(verbose_name='Текст')),
                ('likes', models.IntegerField(default=0, verbose_name='Лайки')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
