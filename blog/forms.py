from django import forms
from .models import Post


class PostForm(forms.ModelForm):   
        
    class Meta:
        model = Post
        fields = [
            'title', 'author', 'info','title_tag', 'blog_image',
            'subheading1', 'main_content1', 'subheading2', 'main_content2'
            ] 

        widgets = {
                'title': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
                # 'author': forms.Select(attrs={'class': 'form-control'}),                
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
            'title', 'author', 'title_tag', 'info', 'blog_image', 'subheading1',
            'main_content1', 'subheading2', 'main_content2'
            ] 

        widgets = {
                'title': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
                # 'author': forms.Select(attrs={'class': 'form-control'}),               
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                'info': forms.TextInput(attrs={'class': 'form-control'}),
                'subheading1': forms.TextInput(attrs={'class': 'form-control'}),
                'main_content1': forms.Textarea(attrs={'class': 'form-control'}),
                'subheading2': forms.TextInput(attrs={'class': 'form-control'}),
                'main_content2': forms.Textarea(attrs={'class': 'form-control'}),
        }