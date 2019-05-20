from django.db import models
from uuid import uuid4

# # Django imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# # Local imports
from .managers import UserManager
import datetime

# # Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=64, blank=False, null=True)
    last_name = models.CharField(_('last name'), max_length=64, blank=False, null=True)
    email = models.EmailField(_('email address'), max_length=256, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_deleted = models.BooleanField(_('deleted'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['date_joined',]

    def get_full_name(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


def key_expire():
	return timezone.now() + datetime.timedelta(days=2)


class AccountSettings(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User')
	activation_key = models.UUIDField(default=uuid4, editable=False)
	key_expire = models.DateTimeField(default=key_expire())

	class Meta:
		verbose_name_plural = "Account Settings"

	def __str__(self):
		return '{}'.format(self.activation_key)


@receiver(post_save, sender=User)
def create_activation_key(sender, instance, created, **kwargs):
	if created:
		AccountSettings.objects.create(user=instance)
