from django import forms
from .models import Post
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Post
        fields = ['title', 'cover','body']
        exclude = ["id"]