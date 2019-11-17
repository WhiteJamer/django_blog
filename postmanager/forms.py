from .models import Post
from django.forms import ModelForm, TextInput, Textarea, SelectMultiple

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        widgets = {
            'title':TextInput(attrs={
                'class':'form-control'
            }),
            'content': Textarea(attrs={
                'class': 'form-control'
            }),
            'categories':SelectMultiple(attrs={
                'class':'form-control'}
            )
        }