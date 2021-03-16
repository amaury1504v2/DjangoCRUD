from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(request):
    context = {'employee_list':Employee.objects.all()} # on charge la liste d'employés via un contexte
    return render(request, "employee_register/employee_list.html", context) # l'objet context est passé en tant que 3è paramètre

def employee_form(request,id=0):
    if request.method == "GET":
        if id==0: 
            form = EmployeeForm() 
        else: 
            employee = Employee.objects.get(pk=id) 
            form = EmployeeForm(instance = employee) 
        return render(request, "employee_register/employee_form.html", {'form':form})
    else:
        if id == 0: #if it is an insert operation
            form = EmployeeForm(request.POST) #it will set an empty form
        else: #if it is an update operation
            employee = Employee.objects.get(pk=id) #it will search the form by id
            form = EmployeeForm(request.POST,instance = employee) #populate the form with the corresponding record details
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')