from django.db import models
from apps.base.models import Timestampable


class Transaction(Timestampable):
    address = models.CharField(max_length=255)
    vhost = models.CharField(max_length=255, default='default')
    agent_ping_time = models.DateTimeField(blank=True)
    time_avg = models.FloatField(default=999, blank=True)

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return self.address

