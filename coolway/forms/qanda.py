# coding: utf-8

from django import forms

class CityForm(forms.Form):
	name = forms.CharField()

	def clean_name(self):
		name = self.cleaned_data['name'] 
		nameLength = len(name)
		if nameLength < 2 or nameLength >6:
			raise forms.ValidationError("城市名称要求在2-6个字之间!") 
		return name