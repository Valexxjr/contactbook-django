from django.views import generic

from .models import Contact


class IndexView(generic.ListView):
    def get_queryset(self):
        return Contact.objects.all()


class DetailView(generic.DetailView):
    model = Contact


class ContactUpdate(generic.UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'patronymic', 'birth_date', 'city']
    template_name_suffix = '_form'

    success_url = '/crud'
