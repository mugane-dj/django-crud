from django.shortcuts import render, redirect
from .forms import InventoryForm
from .models import Inventory

def home(request):
    context = {
        'inventory_list': Inventory.objects.all(), 
        'count': Inventory.objects.count(),
        'perishables': Inventory.objects.filter(material_type='1').count(),
        'disposables': Inventory.objects.filter(material_type='2').count(),
        'non_disposables': Inventory.objects.filter(material_type='3').count()
    }

    return render(request, 'pharmacy/home.html', context)
    
def inventory_form(request, id=0):
    # if id is 0 and its a get request, then it is a new Inventory being registered
    if request.method == "GET":
        if id == 0:
            form = InventoryForm()
        else:
            inventory = Inventory.objects.get(pk=id)
            form = InventoryForm(instance=inventory)
        return render(request, 'pharmacy/material_form.html', {'form': form})
    # if id is not 0 and its a post request, then it is an Inventory being edited
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
    inventory = Inventory.objects.get(pk=id)
    inventory.delete()
    return redirect('inventory_home')


def inventory_search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            inventories = Inventory.objects.filter(material_description__icontains=query)
            return render(request, 'pharmacy/search_db.html', {'inventories': inventories})
    else:
        return render(request, 'pharmacy/search_db.html', {})