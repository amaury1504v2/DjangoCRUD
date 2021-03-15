from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 
        'emp_code', 'mobile', 'position')

        labels = {'fullname': 'Full Name', 
        'emp_code': 'EMP. Code'}

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs) # *args: passer un argument sans mot clé 
        # **kwargs: passer un argument avec mot clé
        self.fields['position'].empty_label = "Select" # on change l'étiquette vide de la table position à Select
        self.fields['emp_code'].required = False # le emp_code n'est pas initialement requis