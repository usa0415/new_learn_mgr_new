from django import forms
from .models import leraning_time

class inputform(forms.ModelForm):
    class Meta:
        model = leraning_time
        fields = ('day','time','category','details')
        widgets = {
            'startdt': forms.DateTimeInput,
            'enddt': forms.DateTimeInput,
        }
        labels = {
            'day': '日付',
            'time': '時間',
            'category': '項目',
            'details':'詳細'
        }