# --coding: utf-8 --
from django import forms
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.Form):
	title=forms.CharField(label=_(u'主题'), max_length=60, widget=forms.TextInput(attrs={'size' : 20, }))
	content=forms.CharField(label=_(u'内容'), max_length=1000, widget=forms.Textarea)
	bonus=forms.CharField(label=_(u'悬赏'), widget=forms.TextInput)

	def is_valid(self):
		#try:
			#bonus_no=int(super.cleaned_data["bonus"])
			#bonus_no=int(super(PostForm, self).clean().get("bonus"))
			#bonus_no=self.cleaned_data.get('bonus')
			bonus_no=int(self['bonus'])
		#except:
			print '1'
			#return False
		#else:
			if super.is_valid() and bonus_no>=0:
				print '2'
				return True
			print '3'
			return False
