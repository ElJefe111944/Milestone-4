from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):   
        
    class Meta:
        model = Post
        fields = [
            'title', 'author', 'info', 'title_tag', 'blog_image',
            'subheading1', 'main_content1', 'subheading2', 'main_content2',
            'subheading3', 'main_content3', 'main_content_extra',
            ] 

        widgets = {
                'title': forms.TextInput(
                    attrs={
                        'class': 'form-control', 'placeholder': 'Blog Title'}),
                # 'author': forms.Select(attrs={'class': 'form-control'}),                
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                'info': forms.TextInput(attrs={'class': 'form-control'}),
                'subheading1': forms.TextInput(
                    attrs={'class': 'form-control'}),
                'main_content1': forms.Textarea(
                    attrs={'class': 'form-control'}),
                'subheading2': forms.TextInput(
                    attrs={'class': 'form-control'}),
                'main_content2': forms.Textarea(
                    attrs={'class': 'form-control'}),
                'subheading3': forms.TextInput(
                    attrs={'class': 'form-control'}),
                'main_content3': forms.Textarea(
                    attrs={'class': 'form-control'}),
                'main_content_extra': forms.Textarea(
                    attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
        
    class Meta:
        model = Post
        fields = [
            'title', 'author', 'title_tag', 'info', 'blog_image', 
            'subheading1',
            'main_content1', 'subheading2', 'main_content2',
            'subheading3', 'main_content3', 'main_content_extra',
            ] 

        widgets = {
                'title': forms.TextInput(
                    attrs={
                        'class': 'form-control', 'placeholder': 'Blog Title'}),
                # 'author': forms.Select(attrs={'class': 'form-control'}),               
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                'info': forms.TextInput(attrs={'class': 'form-control'}),
                'subheading1': forms.TextInput(
                    attrs={'class': 'form-control'}),
                'main_content1': forms.Textarea(
                    attrs={'class': 'form-control'}),
                'subheading2': forms.TextInput(
                    attrs={'class': 'form-control'}),
                'main_content2': forms.Textarea(
                    attrs={'class': 'form-control'}),
                'subheading3': forms.TextInput(
                    attrs={'class': 'form-control'}),
                'main_content3': forms.Textarea(
                    attrs={'class': 'form-control'}),
                'main_content_extra': forms.Textarea(
                    attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
        
    class Meta:
        model = Comment
        fields = ['name', 'comment'] 

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'comment': forms.Textarea(attrs={'class': 'form-control'}),
                }
