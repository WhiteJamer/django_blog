from .models import Post
from django.forms import ModelForm, TextInput, Textarea, SelectMultiple, CharField
from tinymce.widgets import TinyMCE

class PostForm(ModelForm):
    content = CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        widgets = {
            'title':TextInput(attrs={
                'class':'form-control'
            }),
            'categories':SelectMultiple(attrs={
                'class':'form-control'}
            )
        }