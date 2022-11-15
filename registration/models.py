from django.db import models

from home.models import Session

# Create your models here.

"""
A model to accept registration for the session in home app
"""


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    college = models.CharField(max_length=100)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='registrations')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('email', 'session')
