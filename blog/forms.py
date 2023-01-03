from dataclasses import fields
from django import forms
from .models import Post, models

class addpostform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','description','published_at']
