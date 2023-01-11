from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        #fields = ['name', 'lastName', 'email'] # de esta manera se seleccionan los campos q se quieren mostrar en el formulario
        #exclude = ('email',) #Excluye el campo del modelo q no se quiere mostrar en el formulario

