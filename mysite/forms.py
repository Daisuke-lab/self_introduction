from django import forms
from .models import Comment

class CommentForms(forms.ModelForm):
    comment = forms.CharField(required=True, max_length=1000)
    class Meta:
        model = Comment
        fields = "__all__"
