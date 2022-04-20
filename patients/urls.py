from django.urls import path
from patients.views import home, patient_form, patient_delete, patient_search

urlpatterns = [
    path('', home, name='patient_home'),
    path('form/', patient_form, name='patient_insert'),
    path('search/', patient_search, name='patient_search'),
    path('<int:id>/', patient_form, name='patient_update'),
    path('delete/<int:id>', patient_delete, name='patient_delete')
]