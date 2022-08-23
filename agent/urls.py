from django.urls import path
from . import views

app_name = 'agent'

urlpatterns = [
    path('detail/<int:pk>', views.AgentDetailView.as_view(), name='detail_agent'),
    path('all', views.AgentListView.as_view(), name='list_agent'),
]