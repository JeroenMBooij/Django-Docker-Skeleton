from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):

    def create_user(self, email, password):

        if not email:
            raise ValueError("Email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)

        user.save()
        
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff set to True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser set to True')

        return self.create_user(email,password)

class User(AbstractBaseUser):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    username = None
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
