from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, phone_number, password, **extra_fields):
        if not username:
            raise ValueError("Users must have a user name.")
        if not first_name:
            raise ValueError("Users must have a first name.")
        if not phone_number:
            raise ValueError("Users must have a phone number.")
        user = self.model(
            **extra_fields,
            phone_number=phone_number,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, phone_number, password, **extra_fields,):
        user = self.create_user(
            **extra_fields,
            phone_number=phone_number,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=60, unique=True)
    phone_number = models.CharField(
        max_length=11, verbose_name="Phone number", unique=True)
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_joined = models.DateTimeField(
        verbose_name="Date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
