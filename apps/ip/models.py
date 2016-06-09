from django.core.exceptions import ValidationError
from django.db import models
from apps.base.models import Timestampable
from apps.user.models import UserProfile


class IP(Timestampable):
    address = models.URLField(max_length=255)
    vhost = models.CharField(blank=True, max_length=255, default='default')
    user_profile = models.ForeignKey(UserProfile)

    class Meta:
        db_table = 'ips'
        unique_together = ('user_profile', 'address', 'vhost',)

    def save(self, *args, **kwargs):
        if self.address and 'http' in self.address:
            self.address = self.address.split('://')[1].lower()
            if '/' in self.address:
                self.address = self.address.split('/')[0]
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.address



