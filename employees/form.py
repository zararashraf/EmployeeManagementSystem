from .models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'phone', 'emp_code', 'position')
        labels = {
            'name': 'Name',
            'phone': 'Phone',
            'emp_code': 'EMP Code',
            'position': 'Position',
        }