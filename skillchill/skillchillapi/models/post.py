from django.db import models


class Post(models.Model):
    class PostType(models.TextChoices):
        PHOTO = 'P'
        TEXT = 'T'
        VIDEO = 'V'
        LINK = 'L'

    skillager = models.ForeignKey("Skillager", on_delete=models.CASCADE)
    skill = models.ForeignKey("Skill", on_delete=models.DO_NOTHING)
    post_type = models.CharField(max_length=1, choices=PostType.choices)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = ("post")
        verbose_name_plural = ("posts")

    def __str__(self):
        return f'''
        {self.post_type.label} by {self.user.username} for {self.skill.name}
        '''
