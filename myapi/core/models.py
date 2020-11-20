from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django_extensions.db.fields import AutoSlugField


class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    inner_username = AutoSlugField(_('slug'), max_length=50, unique=True, populate_from=('first_name','last_name'))
    role = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    description = models.CharField(max_length=100, blank=True)
    start_work = models.DateField(null=True)
    end_work = models.DateField(null=True)
    wage = models.IntegerField(null=True)

    def __str__(self):
        return self.inner_username



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)