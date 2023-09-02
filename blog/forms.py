from .models import Comment
from django import forms
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'email', 'name', 'comment']