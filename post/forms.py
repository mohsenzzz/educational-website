from django import forms
from ckeditor.fields import CKEditorWidget
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        content = forms.CharField(widget=CKEditorWidget())