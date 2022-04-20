from django.urls import path
from employees.views import home, employee_form, employee_delete, employee_search

urlpatterns = [
    path('', home, name='employee_home'),
    path('form/', employee_form, name='employee_insert'),
    path('search/', employee_search, name='employee_search'),
    path('<int:id>/', employee_form, name='employee_update'),
    path('delete/<int:id>', employee_delete, name='employee_delete')
]

