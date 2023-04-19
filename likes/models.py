from django.db import models
from django.contrib.auth.models import User
from prints.models import Print


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    print = models.ForeignKey(Print, on_delete=models.CASCADE)