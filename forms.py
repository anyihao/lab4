# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:41:26 2015

@author: ANYOHAO
"""
#  制作表单
from django import forms
class BookForm(forms.Form):
    AuthorID = forms.CharField(max_length=20)

    Name = forms.CharField(max_length=40)
    Age = forms.IntegerField()
    Country = forms.CharField(max_length=40)
    ISBN = forms.CharField(max_length=40)
    Title = forms.CharField(max_length=40)
    Publisher = forms.CharField(max_length=40)
    PublishDate = forms.DateField()
    Price = forms.FloatField()
