from django import forms
from django.forms.fields import DateField
from django.core import validators
from django.contrib.auth.models import User
from taskApp.models import UserCustom,UserTask
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime,timedelta

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserCustomForm(forms.ModelForm):
    class Meta():
        model=UserCustom
        fields=('profile_pic',)


class UserTaskForm(forms.ModelForm):
    date=DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'required': 'required'}))
    status=forms.BooleanField(required=False)
    class Meta():
        model=UserTask
        fields=('label','date')

    def clean(self):
        cleaned_data=self.cleaned_data
        date2=cleaned_data.get('date')
        if str(date2)<=(datetime.today()-timedelta(days=1)).strftime('%Y-%m-%d'):
            raise forms.ValidationError("The date cannot be in the past!")
        return cleaned_data
