from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def home(request):
    """
    We're creating a dictionary called context, which contains all the data we want to pass to the
    template. 
    
    The context dictionary contains the following keys:
    
    employee_list: This is a list of all the employees in the database.
    count: This is the total number of employees in the database.
    emails: This is the number of employees who have an email address.
    mobile: This is the number of employees who have a mobile number.
    position: This is the number of employees who have the word "manager" in their position title.
    gender_male: This is the number of male employees.
    gender_female: This is the number of female employees
    
    :param request: The request is a parameter that will be passed to all views by Django. It contains
    metadata about the request, including the HTTP method
    :return: The home function is returning the context variable which is a dictionary.
    """
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
    """
    If the request is a GET request, then we are either creating a new employee or editing an existing
    employee. If the request is a POST request, then we are either creating a new employee or editing an
    existing employee
    
    :param request: The request object is a Django object that contains metadata about the request sent
    to the server
    :param id: the id of the employee being edited, defaults to 0 (optional)
    :return: The employee_form function is returning the employee_home page.
    """
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employees/userform.html', {'form': form})
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
    """
    Get the employee with the primary key of id, delete it, and then redirect to the employee_home page.
    
    :param request: The request is a parameter that is required for all views. It contains metadata
    about the request, including the HTTP method
    :param id: The primary key of the employee we want to delete
    :return: The employee_delete function is returning the redirect function.
    """
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_home')


def employee_search(request):
    """
    If the request method is GET, then get the query from the request, and if the query exists, then
    filter the employees by the query and return the filtered employees
    
    :param request: The request is an HttpRequest object. It contains metadata about the request
    :return: The employee_search function is returning a render of the search_db.html page.
    """
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            employees = Employee.objects.filter(fullname__icontains=query)
            return render(request, 'employees/search_db.html', {'employees': employees})
    else:
        return render(request, 'employees/search_db.html', {})






