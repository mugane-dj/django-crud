from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient 


def home(request):
    context = {
        'patient_list': Patient.objects.all(), 
        'count': Patient.objects.count(),
        'gender_male': Patient.objects.filter(gender='1').count(),
        'gender_female': Patient.objects.filter(gender='2').count()
    }

    return render(request, 'patients/home.html', context)
    
def patient_form(request, id=0):
    # if id is 0 and its a get request, then it is a new patient being registered
    if request.method == "GET":
        if id == 0:
            form = PatientForm()
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(instance=patient)
        return render(request, 'patients/patientform.html', {'form': form})
    # if id is not 0 and its a post request, then it is an patient being edited
    else:
        if id == 0:
            form = PatientForm(request.POST)
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
        return redirect('patient_home')

def patient_delete(request, id):
    patient = Patient.objects.get(pk=id)
    patient.delete()
    return redirect('patient_home')


def patient_search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            patients = Patient.objects.filter(fullname__icontains=query)
            return render(request, 'patients/search_db.html', {'patients': patients})
    else:
        return render(request, 'patients/search_db.html', {})