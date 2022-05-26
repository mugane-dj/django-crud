from django.shortcuts import redirect, render
from employees.models import Employee
from patients.models import Patient
from pharmacy.models import Inventory
from django.http import JsonResponse

def home(request):
    """
    The function home() takes in a request object, and returns a rendered template of the home.html
    file, with the context dictionary passed in.
    
    :param request: The request is an HttpRequest object. It contains metadata about the request. We'll
    see more of this later
    :return: The render function is being returned.
    """ 
    context = {
        'employee_count': Employee.objects.count(),
        'patient_count': Patient.objects.count(),
        'inventory_count': Inventory.objects.count(),
    }
    return render(request, 'web_app/home.html', context )

def chart_1(request):
    """
    We're creating a list of dictionaries, each dictionary containing a key and a value. 
    
    The key is the name of the data we want to display on the chart, and the value is the actual data. 
    
    We're then returning the list of dictionaries as a JSON response. 
    
    The JSON response is what we'll use to populate the chart.
    
    :param request: The request object is passed to the view function by Django. It contains information
    about the current request, such as the HTTP method, the URL, the headers, and the body of the
    request
    :return: A JSON object containing the number of patients and employees.
    """
    chartData = []

    patients = Patient.objects.all().count()
    employees = Employee.objects.all().count()

    chartData.append({'Patients': patients})
    chartData.append({ 'Employees': employees})
    
    return JsonResponse(chartData, safe=False)

def chart_2(request):
    """
    We're creating a list called chartData, and then we're appending to that list the number of items in
    each category
    
    :param request: This is the request object that is sent to the view
    :return: The data is being returned in a JSON format.
    """
    chartData = []

    perishables = Inventory.objects.filter(material_type='1').count(),
    disposables= Inventory.objects.filter(material_type='2').count(),
    non_disposables = Inventory.objects.filter(material_type='3').count()

    chartData.append({'Perishables': perishables[0]})
    chartData.append({ 'Disposables': disposables[0]})
    chartData.append({ 'Non-Disposables': non_disposables})
    
    return JsonResponse(chartData, safe=False)