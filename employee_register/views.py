from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(request):
    context = {'employee_list':Employee.objects.all()} # on charge la liste d'employés via un contexte
    return render(request, "employee_register/employee_list.html", context) # l'objet context est passé en tant que 3è paramètre

def employee_form(request):
    if request.method == "GET":
        form= EmployeeForm()
        return render(request, "employee_register/employee_form.html", {'form':form})
    else:
        form= EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request):
    return