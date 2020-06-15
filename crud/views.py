from django.http import HttpResponse
from django.shortcuts import render

from .models import Contact


def index(request):
    contact_list = Contact.objects.all()
    context = {'contact_list': contact_list}
    return render(request, 'crud/contact_table.html', context)


def detail(request, contact_id):
    return HttpResponse("You're looking at contact %s." % contact_id)

