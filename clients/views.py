from django.shortcuts import render, redirect, get_object_or_404
from .models import Person 
from .forms import ClientForm

# Create your views here.
def clients_list(request):
    clients = Person.objects.all()
    return render(request, 'clients.html',{'clients': clients})

def clients_new(request):
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('clients_list')
    return render(request, 'clients_form.html', {'form': form})

def clients_update(request, id):
    client = get_object_or_404(Person, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('clients_list')

    return render(request, 'clients_form.html', {'form': form})

def clients_delete(request, id):
    client = get_object_or_404(Person, pk=id)
    #form = ClientForm(request.POST or None, request.FILES or None, instance=client)

    if request.method == 'POST':
        client.delete()
        return redirect('clients_list')

    return render(request, 'clients_delete_confirm.html', {'client': client})
