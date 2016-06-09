from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from django.contrib.auth.signals import user_logged_in
from django.conf import settings
from django.apps import apps

from string import digits
from random import choice

from apps.user.models import UserProfile


@receiver(post_save, sender=apps.get_model(settings.AUTH_USER_MODEL))
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    token = ''.join(choice(digits) for i in range(6))
    token = instance.email + ':' + token

    profile = UserProfile.objects.create(user=instance, token=token)
    profile.save()
