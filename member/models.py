
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title