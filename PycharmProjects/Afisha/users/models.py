from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # is_active = models.BooleanField(default=False)
    code = models.CharField(max_length=6)
