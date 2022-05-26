from django.shortcuts import render, redirect
from .forms import InventoryForm
from .models import Inventory

def home(request):
    """
    The function home() takes in a request and returns a render of the home.html page with the context
    of the inventory_list, count, perishables, disposables, and non_disposables
    
    :param request: The request is an HttpRequest object. It contains metadata about the request
    :return: The home page is being returned.
    """
    context = {
        'inventory_list': Inventory.objects.all(), 
        'count': Inventory.objects.count(),
        'perishables': Inventory.objects.filter(material_type='1').count(),
        'disposables': Inventory.objects.filter(material_type='2').count(),
        'non_disposables': Inventory.objects.filter(material_type='3').count()
    }

    return render(request, 'pharmacy/home.html', context)
    
def inventory_form(request, id=0):
    """
    If the request is a GET request, then if the id is 0, create a new form, otherwise get the inventory
    with the given id and create a form with that inventory. 
    
    If the request is a POST request, then if the id is 0, create a new form with the POST data,
    otherwise get the inventory with the given id and create a form with the POST data and the
    inventory. 
    
    If the form is valid, save it. 
    
    Finally, redirect to the inventory home page.
    
    :param request: The request object is an HttpRequest object. It contains metadata about the request,
    including the HTTP method
    :param id: The id of the inventory item to be edited. If it's 0, then it's a new item, defaults to 0
    (optional)
    :return: The inventory_home function is returning the inventory_home.html page.
    """
    if request.method == "GET":
        if id == 0:
            form = InventoryForm()
        else:
            inventory = Inventory.objects.get(pk=id)
            form = InventoryForm(instance=inventory)
        return render(request, 'pharmacy/material_form.html', {'form': form})
    else:
        if id == 0:
            form = InventoryForm(request.POST)
        else:
            inventory = Inventory.objects.get(pk=id)
            form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
        return redirect('inventory_home')

def inventory_delete(request, id):
    """
    It deletes the inventory object with the primary key of id
    
    :param request: This is the request object that is sent to the view
    :param id: The primary key of the inventory item to be deleted
    :return: The inventory_delete function is returning the redirect function.
    """
    inventory = Inventory.objects.get(pk=id)
    inventory.delete()
    return redirect('inventory_home')


def inventory_search(request):
    """
    If the request is a GET request, then get the query from the request and if the query exists, then
    filter the Inventory objects by the material description and return the filtered inventories
    
    :param request: The request is an HttpRequest object
    :return: The search_db.html page is being returned.
    """
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            inventories = Inventory.objects.filter(material_description__icontains=query)
            return render(request, 'pharmacy/search_db.html', {'inventories': inventories})
    else:
        return render(request, 'pharmacy/search_db.html', {})