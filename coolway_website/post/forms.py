# -*- encoding: utf-8 -*-
from django import forms


class PostCreateForm(forms.Form):
    """发帖"""
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=1000)


class ReplyForm(forms.Form):
    """ 帖子回复"""
    content = forms.CharField(required=True,max_length=500, label=u'回复')

