# --coding: utf-8 --
from django import forms
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.Form):
	title=forms.CharField(label=_(u'主题'),max_length=60,widget=forms.TextInput(attrs={'size':20,}))
	content=forms.CharField(label=_(u'内容'),max_length=10000,widget=forms.Textarea)
