from django import forms
from .models import ContactModel


class ContactPostForm(forms.Form):
    CHOICES = (('friends', 'Friends'),
               ('search_engine', 'Search Engine'),
               ('ads', 'Advertisment'),
               ('other', 'Others'))
    name = forms.CharField(label='Name', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Email address'}))
    found_by = forms.CharField(required=False,  widget=forms.Select(choices=CHOICES,
                                                                    attrs={'placeholder': 'Found Us'}))
    receive_newsletter = forms.BooleanField()
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Message'}
    ))

    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'found_by', 'receive_newsletter', 'message']

    def save(self):
        data = self.cleaned_data
        user = ContactModel(email=data['email'], name=data['name'],
                       found_by=data['found_by'], receive_newsletter=data['receive_newsletter'], message=data['message'])
        user.save()
