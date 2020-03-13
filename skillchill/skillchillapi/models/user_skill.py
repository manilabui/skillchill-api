from django.db import models
from django.contrib.auth.models import User


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey("Skill", on_delete=models.CASCADE)
    is_moderator = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = ("user skill")
        verbose_name_plural = ("user skills")

    def __str__(self):
        return f'''
        User: {self.user.username}
        Skill: {self.name}
        Moderator: {self.is_moderator}
        '''
