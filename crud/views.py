from django.http import HttpResponse
from django.template import loader

from .models import Contact


def index(request):
    contact_list = Contact.objects.all()
    template = loader.get_template('crud/contact_table.html')
    context = {
        'contact_list': contact_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, contact_id):
    return HttpResponse("You're looking at contact %s." % contact_id)

