from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext as _
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token


class TeamMember(AbstractUser):
    role = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    start_work = models.DateField(null=True)
    end_work = models.DateField(null=True)
    wage = models.IntegerField(null=True)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)