from socket import fromshare
from django import forms
from .models import Comment, Message

class CommentForm(forms.ModelForm):
    required_css_class = 'tm-color-primary'
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class MessageForm(forms.ModelForm):
    required_css_class = 'tm-color-primary'

    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'message')