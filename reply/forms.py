# --coding: utf-8 --
from django import forms
from django.utils.translation import ugettext_lazy as _

class ReplyForm(forms.Form):
	content = forms.CharField(label=_(u'内容'), max_length=400, widget=forms.Textarea)
	reply_tag = forms.CharField(widget=forms.HiddenInput())

	def valid(self):
		'''check the validation of ReplyForm

		check if the content length valid'''

		print 'form', self.is_valid()
		if self.is_valid():
			content = self.cleaned_data["content"]
			if len(content) <= 400:
				return True
		return False
