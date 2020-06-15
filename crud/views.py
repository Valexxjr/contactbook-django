from django.shortcuts import get_object_or_404, render

from .models import Contact


def index(request):
    contact_list = Contact.objects.all()
    context = {'contact_list': contact_list}
    return render(request, 'crud/contact_table.html', context)


def detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'crud/contact.html', {'contact': contact})