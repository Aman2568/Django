from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    Published_date = models.DateTimeField(blank = True , null = True)

    def __str__(self):
        return self.title