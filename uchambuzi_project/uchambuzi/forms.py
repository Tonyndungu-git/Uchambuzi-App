# uchambuzi/forms.py

from django import forms

class DataCollectionForm(forms.Form):
    file = forms.FileField(label='Select a file', help_text='CSV or Excel file')
