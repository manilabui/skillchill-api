from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=128)
    avatar = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = ("skill")
        verbose_name_plural = ("skills")

    def __str__(self):
        return self.name
