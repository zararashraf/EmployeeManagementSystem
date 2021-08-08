from employees.form import EmployeeForm
from django.shortcuts import render, redirect
from .models import Employee

def create(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')

    return render(request, 'employee/create.html', { 'form': form })

def read(request):
    employees = Employee.objects.all()
    return render(request, 'employee/read.html', { 'employees': employees })

def update(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('read')

    return render(request, 'employee/create.html', { 'form': form })

def delete(request, emp_id):
    employee = Employee.objects.get(pk=emp_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('read')
        
    return render(request, 'employee/read.html')