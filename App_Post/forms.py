from django import forms

from App_Post import models


class PostModelForm(forms.ModelForm):

    class Meta:
        model = models.PostModel
        fields = ['post_image', 'caption']
