from django.forms import ModelForm, TextInput, FileInput
from .models import User

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar']
        widgets = {
            # 'username':TextInput()
            # 'avatar':FileInput(attrs={'class':'form-control'})
        }