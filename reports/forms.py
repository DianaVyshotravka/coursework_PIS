from django import forms

from reports.models import Report


class NewReport(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'description', 'project', 'file']
        widgets = {
            'name': forms.TextInput(),
            'description': forms.TextInput(),
            'project': forms.TextInput(),
            'file': forms.FileInput()
        }