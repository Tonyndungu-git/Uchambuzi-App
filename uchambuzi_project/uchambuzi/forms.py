# uchambuzi/forms.py

from django import forms

class DataCollectionForm(forms.Form):
    file = forms.FileField(label='Select a file', help_text='CSV or Excel file')

class ColumnSelectionForm(forms.Form):
    def __init__(self, *args, columns=[], **kwargs):
        super(ColumnSelectionForm, self).__init__(*args, **kwargs)
        self.fields['x_axis'] = forms.ChoiceField(choices=[(column, column) for column in columns])
        self.fields['y_axis'] = forms.ChoiceField(choices=[(column, column) for column in columns])