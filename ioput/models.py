from django.db import models
from django.utils import timezone
from datetime import date


class leraning_time(models.Model):
    id = models.AutoField
    day = models.DateField(default= timezone.now)
    time = models.IntegerField(blank= False, null=True)
    category = models.CharField(default="", max_length=200)
    details = models.CharField(default="", max_length=200, blank=True, null=True)
    startdt = models.DateTimeField(default=timezone.now)
    enddt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.category

'''
    def save(self, *args, **kwargs):
        self.dt = self.enddt - self.startdt
        super(leraning_time, self).save(*args, **kwargs)
'''