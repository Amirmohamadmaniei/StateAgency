from django.urls import reverse, reverse_lazy
from django.views import generic
from agent.models import Agent
from blog.models import Blog
from home import forms
from home.models import Contact, SocialNetwork
from house.models import Property


class HomeView(generic.TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        properties = Property.objects.all()[:5]
        agents = Agent.objects.all()[:3]
        blogs = Blog.objects.all().order_by('-created')[:5]
        context['last_properties'] = properties
        context['best_agents'] = agents
        context['last_blogs'] = blogs
        return context


class AboutView(generic.TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        agents = Agent.objects.all()[:3]
        context['best_agents'] = agents
        return context


class ContactView(generic.FormView):
    template_name = 'home/contact.html'
    form_class = forms.ContactForm
    success_url = reverse_lazy('home:contact')

    def form_valid(self, form):
        Contact.objects.create(
            full_name=form.cleaned_data.get('full_name'),
            email=form.cleaned_data.get('email'),
            sub=form.cleaned_data.get('sub'),
            body=form.cleaned_data.get('body'),
        )
        return super(ContactView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['social_network'] = SocialNetwork.objects.all().first()
        return context
