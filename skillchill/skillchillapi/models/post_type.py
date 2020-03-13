from django.db import models


class PostType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("name",)
        verbose_name = ("post type")
        verbose_name_plural = ("post types")

    def __str__(self):
        return self.name
