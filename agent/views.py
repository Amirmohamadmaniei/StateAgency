from django.views.generic import DetailView, ListView
from .models import Agent


class AgentDetailView(DetailView):
    model = Agent


class AgentListView(ListView):
    model = Agent
    paginate_by = 1
