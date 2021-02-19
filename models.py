from django.db import models
from django.contrib.auth.models import User
# from .forms import ModelForm

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='images/')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     author = models.CharField(max_length=60)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey('Post', on_delete=models.CASCADE)

class CategoryToPost(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE  )
    category = models.ForeignKey('Category', on_delete=models.CASCADE )
# # class PostForm(ModelForm):
#     required_css_class = 'required'

#     class Meta:
#         model = Post
#         exclude = ['id']