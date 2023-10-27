# from django.db import models

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "auth_user"
        verbose_name_plural = "auth_user"

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)













# # Create your models here.
# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class Users(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     email = models.CharField(unique=True, max_length=255)
#     father = models.CharField(max_length=255)
#     father_phone_number = models.BigIntegerField(blank=True, null=True)
#     mother_name = models.CharField(max_length=255, blank=True, null=True)
#     mother_phone_number = models.BigIntegerField(blank=True, null=True)
#     phone_number = models.BigIntegerField(blank=True, null=True)
#     gender = models.CharField(max_length=255)
#     date_of_birth = models.CharField(max_length=255)
#     uan_no = models.BigIntegerField(blank=True, null=True)
#     employee_no = models.IntegerField()
#     date_of_joining = models.CharField(max_length=255, blank=True, null=True)
#     probation_period = models.CharField(max_length=255, blank=True, null=True)
#     department = models.CharField(max_length=255, blank=True, null=True)
#     designation = models.CharField(max_length=255, blank=True, null=True)
#     qualification = models.CharField(max_length=255, blank=True, null=True)
#     degree = models.CharField(max_length=255, blank=True, null=True)
#     status = models.IntegerField()
#     type = models.IntegerField(blank=True, null=True)
#     salary = models.BigIntegerField(blank=True, null=True, db_comment='basic_salary or starting-salary of user')
#     current_salary = models.BigIntegerField(db_comment='current_salary of user')
#     payble = models.BigIntegerField(blank=True, null=True)
#     email_verified_at = models.DateTimeField(blank=True, null=True)
#     password = models.CharField(max_length=255)
#     remember_token = models.CharField(max_length=100, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     device_token = models.TextField(blank=True, null=True)
#     screenshot_preview = models.IntegerField(db_comment='1=>show,0=>hide')

#     class Meta:
#         managed = False
#         db_table = 'users'

