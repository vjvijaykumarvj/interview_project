from django import forms
from.models import Employee

class Emp_form(forms.ModelForm):
    # eno = forms.IntegerField()
    # name = forms.CharField(max_length=100)
    # age = forms.IntegerField()
    # salary = forms.IntegerField()
    # address = forms.CharField(max_length=400)
    class Meta:
        model = Employee
        fields = '__all__'