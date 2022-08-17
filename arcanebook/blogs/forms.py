from dataclasses import fields
from pyexpat import model
from django import forms
from froala_editor.widgets import FroalaEditor
from .models import BlogModel


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content']