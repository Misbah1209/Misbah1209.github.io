from django import forms
from django.db import models
from django.contrib.auth.models import User
from rango.models import UserProfile,Tip,Outfit,List,Item

#Creating forms used to upload functions
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ( 'username','email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('telephone',)

class TipForm(forms.ModelForm):

    class Meta:
        model= Tip
        fields=['category','title','img','content','likes']
        label = {
                'title': ('Title'),
                'likes': ('Likes'),
                'content': ('Content'),
                'img': ('Image'),
                'category':('Category')
            }
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not (url.startswith('http://') or url.startswith('https://')):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data

class ListForm(forms.ModelForm): 
    class Meta:
        model = List
        fields = ( 'name',)

class ItemForm(forms.ModelForm): 
    class Meta:
        model = Item
        fields = ( 'title',)

class OutfitForm(forms.ModelForm):

    class Meta:
        model= Outfit
        
        fields=['season','name','image','description']
        label = {
                'name': ('Name'),
                'season': ('Season'),
                'image': ('Image'),
                'description':('Description')
            }
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not (url.startswith('http://') or url.startswith('https://')):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data