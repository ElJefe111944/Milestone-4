from django import forms
from watches.widgets import (
    CustomClearableFileInput)
from .models import Post


class PostForm(forms.ModelForm):
        
    class Meta:
        model = Post
        fields = [
            'title', 'author', 'title_tag', 'blog_image', 'subheading1',
            'main_content1', 'subheading2', 'main_content2'
            ] 

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'author': forms.Select(attrs={'class': 'form-control'}),
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),                
                'subheading1': forms.TextInput(attrs={'class': 'form-control'}),
                'main_content1': forms.Textarea(attrs={'class': 'form-control'}),
                'subheading2': forms.TextInput(attrs={'class': 'form-control'}),
                'main_content2': forms.Textarea(attrs={'class': 'form-control'}),
        }