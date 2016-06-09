from django.db import models
from apps.base.models import Timestampable

# Create your models here.

class Landing(Timestampable):
    email = models.EmailField(blank=False, max_length=255, unique=True)

    class Meta:
        db_table = 'landing'

    def __str__(self):
        return self.email
