from django.urls import path
from .views import home, inventory_form, inventory_delete, inventory_search

urlpatterns = [
    path('', home, name='inventory_home'),
    path('form/', inventory_form, name='inventory_insert'),
    path('search/', inventory_search, name='inventory_search'),
    path('<int:id>/', inventory_form, name='inventory_update'),
    path('delete/<int:id>', inventory_delete, name='inventory_delete')
]
