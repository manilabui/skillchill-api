from django.db import models
from django.contrib.auth.models import User


class Skillager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name = ("skillager")
        verbose_name_plural = ("skillagers")

    def __str__(self):
        return {self.user.username}
