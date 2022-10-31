from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import Profile

class profileRgister(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'