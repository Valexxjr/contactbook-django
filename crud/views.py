from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from .models import Contact, Phone, Attachment


class IndexView(generic.ListView):
    def get_queryset(self):
        return Contact.objects.all()


class DetailView(generic.DetailView):
    model = Contact


class ContactUpdate(generic.UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'patronymic', 'birth_date', 'city', 'country', 'citizenship']
    template_name_suffix = '_form'

    def get_success_url(self):
        return reverse('crud:contact_detail', kwargs={'pk': self.kwargs.get('pk')})


class PhoneUpdate(generic.UpdateView):
    model = Phone
    fields = ['phone_number', 'operator_code', 'country_code', 'note']
    template_name_suffix = '_form'

    def get_success_url(self):
        return reverse('crud:contact_detail', kwargs={'pk': self.kwargs.get('contact_id')})


class PhoneCreate(generic.CreateView):
    model = Phone
    fields = ['phone_number', 'operator_code', 'country_code', 'note']
    template_name_suffix = '_form'

    def form_valid(self, form):
        form.instance.contact = Contact.objects.get(id=self.kwargs.get('pk'))
        return super(PhoneCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('crud:contact_detail', kwargs={'pk': self.kwargs.get('pk')})


class AttachmentUpdate(generic.UpdateView):
    model = Attachment
    fields = ['file_name', 'upload_date', 'note']
    template_name_suffix = '_form'

    def get_success_url(self):
        return reverse('crud:contact_detail', kwargs={'pk': self.kwargs.get('contact_id')})


class AttachmentCreate(generic.CreateView):
    model = Attachment
    fields = ['file_name', 'upload_date', 'note']
    template_name_suffix = '_form'

    def form_valid(self, form):
        form.instance.contact = Contact.objects.get(id=self.kwargs.get('pk'))
        return super(AttachmentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('crud:contact_detail', kwargs={'pk': self.kwargs.get('pk')})


def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('crud:index')


def delete_phone(request, contact_id, pk):
    phone = Phone.objects.get(pk=pk)
    phone.delete()
    return HttpResponseRedirect(reverse('crud:contact_detail', args=(contact_id,)))


def delete_attachment(request, contact_id, pk):
    attachment = Attachment.objects.get(pk=pk)
    attachment.delete()
    return HttpResponseRedirect(reverse('crud:contact_detail', args=(contact_id,)))
