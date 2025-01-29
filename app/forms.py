from django import forms
from .models import Contact, Video, Image, Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
