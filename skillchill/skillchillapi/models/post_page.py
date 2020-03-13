from django.db import models


class PostPage(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    caption = models.CharField(max_length=2000)
    page_num = models.IntegerField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ("page_num",)
        verbose_name = ("post page")
        verbose_name_plural = ("post pages")

    def __str__(self):
        return self.page_num
