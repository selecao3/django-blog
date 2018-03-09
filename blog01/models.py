from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def Body(self):
        return self.body[:30]

# Create your models here.
