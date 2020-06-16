from django.views import generic

from .models import Contact


class IndexView(generic.ListView):
    def get_queryset(self):
        return Contact.objects.all()


class DetailView(generic.DetailView):
    model = Contact
