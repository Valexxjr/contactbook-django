from django.views import generic

from .models import Contact


class IndexView(generic.ListView):
    def get_queryset(self):
        return Contact.objects.all()


class DetailView(generic.DetailView):
    model = Contact

# def index(request):
#     contact_list = Contact.objects.all()
#     context = {'contact_list': contact_list}
#     return render(request, 'crud/contact_list.html', context)


# def detail(request, contact_id):
#     contact = get_object_or_404(Contact, pk=contact_id)
#     return render(request, 'crud/contact_detail.html', {'contact': contact})