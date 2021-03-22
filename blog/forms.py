from django import forms
from watches.widgets import (
    CustomClearableFileInput)
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):   
        
    class Meta:
        model = Post
        fields = [
            'title', 'author', 'info',  'category', 'title_tag', 'blog_image',
            'subheading1', 'main_content1', 'subheading2', 'main_content2'
            ] 

        widgets = {
                'title': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
                # 'author': forms.Select(attrs={'class': 'form-control'}),
                'category': forms.Select(
                    choices=choice_list, attrs={'class': 'form-control'}),
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                'info': forms.TextInput(attrs={'class': 'form-control'}),
                'subheading1': forms.TextInput(attrs={'class': 'form-control'}),
                'main_content1': forms.Textarea(attrs={'class': 'form-control'}),
                'subheading2': forms.TextInput(attrs={'class': 'form-control'}),
                'main_content2': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
        
    class Meta:
        model = Post
        fields = [
            'title', 'author', 'category', 'title_tag', 'info', 'blog_image', 'subheading1',
            'main_content1', 'subheading2', 'main_content2'
            ] 

        widgets = {
                'title': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
                # 'author': forms.Select(attrs={'class': 'form-control'}),
                'category': forms.Select(
                    choices=choice_list, attrs={'class': 'form-control'}),
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                'info': forms.TextInput(attrs={'class': 'form-control'}),
                'subheading1': forms.TextInput(attrs={'class': 'form-control'}),
                'main_content1': forms.Textarea(attrs={'class': 'form-control'}),
                'subheading2': forms.TextInput(attrs={'class': 'form-control'}),
                'main_content2': forms.Textarea(attrs={'class': 'form-control'}),
        }