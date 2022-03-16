from django.urls import path
from web_app.views import employee_form, employee_delete, employee_search

urlpatterns = [
    path('form/', employee_form, name='employee_insert'),
    path('search/', employee_search, name='employee-search'),
    path('<int:id>/', employee_form, name='employee_update'),
    path('delete/<int:id>', employee_delete, name='employee_delete')
]
