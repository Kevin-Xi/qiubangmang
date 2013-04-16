# --coding: utf-8 --
from django import forms
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.Form):
	title=forms.CharField(label=_(u'主题'), max_length=60, widget=forms.TextInput(attrs={'size' : 20, }))
	content=forms.CharField(label=_(u'内容'), max_length=1000, widget=forms.Textarea)
	bonus=forms.CharField(label=_(u'悬赏'), widget=forms.TextInput)

	def valid(self):
		if self.is_valid():
			try:
				bonus_no=int(self.cleaned_data['bonus'])
				if bonus_no>=0:
					return True
			except:
				return False
		return False
