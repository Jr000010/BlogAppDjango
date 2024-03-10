# blog/models.py

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to='post_images/')
    post_image_caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
