from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    skillager = models.ForeignKey("Skillager", on_delete=models.CASCADE)
    skill = models.ForeignKey("Skill", on_delete=models.DO_NOTHING)
    post_type = models.ForeignKey("PostType", on_delete=models.DO_NOTHING)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = ("post")
        verbose_name_plural = ("posts")

    def __str__(self):
        return f'''
        Post by {self.user.username} for {self.skill.name}
        '''
