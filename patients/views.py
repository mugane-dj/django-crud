from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient 


def home(request):
    """
    The function home() takes in a request and returns a render of the home.html page with the context
    of the list of patients, the number of patients, and the number of male and
    female patients.   
    :param request: This is the request object that is sent to the view
    :return: The home function is returning the render function.
    """
    context = {
        'patient_list': Patient.objects.all(), 
        'count': Patient.objects.count(),
        'gender_male': Patient.objects.filter(gender='1').count(),
        'gender_female': Patient.objects.filter(gender='2').count()
    }

    return render(request, 'patients/home.html', context)
    
def patient_form(request, id=0):
    """
    If the request is a GET request, then we either create a new form or populate an existing form with
    data from the database. 
    
    If the request is a POST request, then we either create a new record or update an existing record in
    the database.
    
    :param request: The request object is an object that contains information about the current request
    :param id: The id of the patient to be edited. If it's 0, then it's a new patient, defaults to 0
    (optional)
    :return: The patient_form function is returning the patientform.html page.
    """
    if request.method == "GET":
        if id == 0:
            form = PatientForm()
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(instance=patient)
        return render(request, 'patients/patientform.html', {'form': form})
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
    """
    It deletes a patient from the database
    
    :param request: This is the request object that is sent to the view
    :param id: The id of the patient to be deleted
    :return: The patient_delete function is returning the redirect function, which is redirecting the
    user to the patient_home page.
    """
    patient = Patient.objects.get(pk=id)
    patient.delete()
    return redirect('patient_home')


def patient_search(request):
    """
    If the request is a GET request, then get the query from the request and if the query exists, then
    filter the patients by the query and return the filtered patients
    
    :param request: The request object is an HttpRequest object. It contains metadata about the request,
    including the HTTP method, host, path, and more
    :return: The search_db.html template is being returned.
    """
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            patients = Patient.objects.filter(fullname__icontains=query)
            return render(request, 'patients/search_db.html', {'patients': patients})
    else:
        return render(request, 'patients/search_db.html', {})