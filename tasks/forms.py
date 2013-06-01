# --coding: utf-8 --
from django import forms
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.Form):
	title=forms.CharField(label=_(u'主题'), max_length=80, widget=forms.TextInput(attrs={'size' : 20, }))
	content=forms.CharField(label=_(u'内容'), max_length=1000, widget=forms.Textarea)
	bonus=forms.CharField(label=_(u'悬赏'), widget=forms.TextInput)
	deadline = forms.CharField(label=_(u'截止日期'), widget=forms.TextInput)

	def valid(self):
		if self.is_valid():
			try:
				bonus_no=int(self.cleaned_data['bonus'])
				title=self.cleaned_data["title"]
				content=self.cleaned_data["content"]
				if bonus_no>=0 and len(title) <= 80 and len(content) <= 1000:
					return True
			except:
				return False
		return False
