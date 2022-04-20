from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def home(request):
    context = {
        'employee_list': Employee.objects.all(), 
        'count': Employee.objects.count(),
        'emails': Employee.objects.filter(email__contains='@').count(),
        'mobile': Employee.objects.filter(mobile__contains='+').count(),
        'position': Employee.objects.filter(position__title__icontains='manager').count(),
        'gender_male': Employee.objects.filter(gender='1').count(),
        'gender_female': Employee.objects.filter(gender='2').count()
    }
    return render(request, 'employees/home.html', context)

def employee_form(request, id=0):
    # if id is 0 and its a get request, then it is a new employee being registered
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employees/userform.html', {'form': form})
    # if id is not 0 and its a post request, then it is an employee being edited
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee_home')

def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_home')


def employee_search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            employees = Employee.objects.filter(fullname__icontains=query)
            return render(request, 'employees/search_db.html', {'employees': employees})
    else:
        return render(request, 'employees/search_db.html', {})






