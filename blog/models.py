from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from embed_video.fields import EmbedVideoField
from ckeditor_uploader.fields import RichTextUploadingField
from bs4 import BeautifulSoup


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video_url = models.URLField(blank=True, null=True)



    def get_first_image(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        img = soup.find('img')
        if img and img.get('src'):
            return img['src']
        return None

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comentariu de la {self.user.username} la {self.post.title}"


class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_liked = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('post', 'user')  # Un user poate da like o singură dată la o postare

    def __str__(self):
        return f"{self.user.username} a dat like la {self.post.title}"
