from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.core.validators import *
from django.db import models

user_type = (('1', 'Клиент'), ('2', 'Фотограф'))
default_bio = 'Задача организации, в особенности же перспективное планирование не даёт нам иного выбора, кроме определения переосмысления внешнеэкономических политик. Для современного мира синтетическое тестирование выявляет срочную потребность инновационных методов управления процессами. Являясь всего лишь частью общей картины, ключевые особенности структуры проекта набирают популярность среди определенных слоев населения, а значит, должны быть в равной степени предоставлены сами себе.'
default_tech = 'Без Зеркальная камера EOS R5'

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = models.CharField(max_length=256, blank=False, null=False, unique=True, verbose_name='Имя Пользователя')
    email = models.EmailField(blank=False, null=False, unique=True, validators=[EmailValidator], verbose_name='Электронная почта')
    name = models.CharField(max_length=256, blank=False, null=False, verbose_name='Имя')
    surname = models.CharField(max_length=256, blank=False, null=False, verbose_name='Фамилия')
    password = models.CharField(max_length=256, blank=False, null=False, validators=[MinLengthValidator(8, "Пароль должен быть не меньше 8 символов"),
                                                                                     MaxLengthValidator(256, "Пароль должен быть не более 256 символов")])

    object = CustomUserManager()

    user_type = models.CharField(max_length=64, blank=False, null=False, choices=(user_type), default='1', verbose_name='Тип Пользователя')
    # agreement = models.BooleanField(blank=False ,verbose_name='Соглашение')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_anonymous = False
    is_authenticated = True

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)


class Photographer(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, verbose_name='Пользователь')
    photo = models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/', default='default/default_profile_image.png', verbose_name='Фотография')
    bio = models.TextField(blank=True, null=True, default=default_bio, verbose_name='Биография')
    tech = models.CharField(max_length=256, blank=True, null=True, default=default_tech, verbose_name='Техника')

    def clearUsername(self):
        return self.user_id.username

    def __str__(self):
        return f'{self.user_id.name} {self.user_id.surname}'


class Review(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, verbose_name='Пользователь')
    text_content = models.TextField(blank=False, null=False, verbose_name='Текст')
    likes = models.IntegerField(default=0, verbose_name='Лайки')

    def Username(self):
        return self.user_id.username


photosession_type = (('1', 'Портрет.'),
                     ('2', 'Фотоссестия Пары (Love Story).'),
                     ('3', 'Репортаж.'),
                     ('4', 'Fashion.'),
                     ('5', 'Предметная Фотография.'),
                     ('6', 'Пейзаж.'),
                     ('7', 'Архитектурная Фотография.'),
                     ('8', 'Стиль "ню".'),
                     ('9', 'Фотографии детей.'),
                     ('10', 'Съёмка домашних животных или диких животных.'),
                     ('11', 'Свадебная фотосессия.'),
                     ('12', 'Фотосъёмка беременных.'),
                     ('13', 'Макросъёмка.')
                     )


class Reservation(models.Model):
    email = models.CharField(max_length=256, blank=False, null=False, verbose_name='* Электронная почта')
    description = models.TextField(blank=False, null=True, verbose_name='* Описание')
    phone_number = models.CharField(max_length=32, blank=True, null=True, validators=[RegexValidator('/^\+?(\d{1,3})?[- .]?\(?(?:\d{2,3})\)?[- .]?\d{3}?\d{3}$/')], verbose_name='Телефон')
    photograph_id = models.ForeignKey(Photographer, on_delete=models.CASCADE, blank=False, verbose_name='* Фотограф')
    photosession_type = models.CharField(max_length=64, blank=False, null=False, choices=(photosession_type), default='1', verbose_name='* Тип фотосессии')

    example = models.ImageField(blank=True, null=True, verbose_name='Примеры')

    def EmailUser(self):
        user = CustomUser.object.get(email=self.email)
        return user.username