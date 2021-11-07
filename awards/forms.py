from django.contrib.auth import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from .models import Project, Profile, Rating
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field


class ProjectForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('post', 'post',css_class = 'btn btn-success'))

    class Meta:
        model = Project
        fields = [
            'title',
            'image',
            'description',
            'link',

        ]
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture',
                  'bio',
                  'contact'
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class RateForm(forms.ModelForm):

    class Meta:
        model= Rating
        field=['design', 'usability', 'content']
        exclude=['project', 'author']