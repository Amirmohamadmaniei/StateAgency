from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from .forms import RequestVisitForm
from .models import Property, RequestVisit
from django.db.models import Q


class PropertyDetailView(FormMixin, DetailView):
    model = Property
    form_class = RequestVisitForm
    success_url = '/'

    def get_success_url(self):
        return reverse('property:detail_property', kwargs={'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        RequestVisit.objects.create(phone=phone, email=email, message=message,
                                    user=self.request.user, agent=self.object.agent,
                                    property=self.object)
        return super(PropertyDetailView, self).form_valid(form)


class PropertyListView(ListView):
    model = Property
    paginate_by = 2


class PropertySearchListView(ListView):
    model = Property
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PropertySearchListView, self).get_context_data(object_list=None, **kwargs)
        q = self.request.GET.get('q')
        context['object_list'] = Property.objects.filter(title__icontains=q)
        return context
