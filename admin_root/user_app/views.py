from django.shortcuts import render, redirect
from.models import Employee
from.forms import Emp_form
# Create your views here.

def Register(request):
    if request.method == 'GET':
        Employee_list = Employee.objects.all()
        emp_form = Emp_form()

        dict = {
            'employee_list'  : Employee_list,
            'form' : emp_form
        }
        return render(request,'user_app/register.html',context=dict)
    elif request.method =='POST':
        form = Emp_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/register/')
def updating(request,pk):
    if request.method  == 'GET':
        employee = Employee.objects.get(id=pk)
        emp_form = Emp_form(instance=employee)
        emp_list = Employee.objects.all()
        dict = {
            'form' : emp_form,
            'Employee_list' : emp_list,
            'is_update' : 'yes'
        }
        return render(request,'user_app/register.html',context=dict)
    elif request.method == 'POST':
        employee  = Employee.objects.get(id=pk)
        emp_form = Emp_form(request.POST,instance=employee)
        if emp_form.is_valid():
            emp_form.save()
            return redirect('/user/register/')
def deleting(request,pk):
    employee  = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/user/register/')





