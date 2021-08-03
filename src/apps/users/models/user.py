from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyUserManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError("Email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)

        user.save(using=self._db)
        
        return user
        
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff set to True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser set to True')

        return self.create_user(email, password, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=255)
    email = models.EmailField('email address', unique=True)
    username = None
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
