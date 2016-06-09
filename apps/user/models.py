from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

class UserProfile(models.Model):
    TRIAL_USER = 1
    PREMIUM_USER = 2
    USER_STATUS = (
        (TRIAL_USER, 'Free User'),
        (PREMIUM_USER, 'Premium User'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile', primary_key=True)
    subscription = models.IntegerField(choices=USER_STATUS, default=TRIAL_USER)
    expired_date = models.DateTimeField(auto_now_add=True)
    token = models.CharField(blank=True, max_length=255)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.user.email
