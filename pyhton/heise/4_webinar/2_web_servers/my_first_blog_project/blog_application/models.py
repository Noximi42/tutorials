from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_modified_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        # noinspection PyUnresolvedReferences
        return f'{self.id} | {self.title} | {timezone.localtime(self.last_modified_timestamp)}'


class Comment(models.Model):
    blog_post = models.ForeignKey(to=BlogPost, on_delete=models.CASCADE)  # many-to-one relationship
    author = models.CharField(max_length=80)
    e_mail_address = models.CharField(max_length=50, default=None)
    content = models.TextField()

    def __str__(self):
        return f'{self.author} ==> {self.blog_post}'
