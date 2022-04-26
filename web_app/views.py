from django.shortcuts import redirect, render
from employees.models import Employee
from patients.models import Patient
from pharmacy.models import Inventory
from django.http import JsonResponse

def home(request):
    context = {
        'employee_count': Employee.objects.count(),
        'patient_count': Patient.objects.count(),
        'inventory_count': Inventory.objects.count(),
    }
    return render(request, 'web_app/home.html', context )

def chart_1(request):
    chartData = []

    patients = Patient.objects.all().count()
    employees = Employee.objects.all().count()

    chartData.append({'Patients': patients})
    chartData.append({ 'Employees': employees})
    
    return JsonResponse(chartData, safe=False)

def chart_2(request):
    chartData = []

    perishables = Inventory.objects.filter(material_type='1').count(),
    disposables= Inventory.objects.filter(material_type='2').count(),
    non_disposables = Inventory.objects.filter(material_type='3').count()

    chartData.append({'Perishables': perishables[0]})
    chartData.append({ 'Disposables': disposables[0]})
    chartData.append({ 'Non-Disposables': non_disposables})
    
    return JsonResponse(chartData, safe=False)