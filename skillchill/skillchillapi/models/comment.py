from django.db import models


class Comment(models.Model):
    skillager = models.ForeignKey("Skillager", on_delete=models.DO_NOTHING)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(blank=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = ("comment")
        verbose_name_plural = ("comments")

    def __str__(self):
        return f'''
        Comment by {self.user.username} for {self.post.name}
        '''
