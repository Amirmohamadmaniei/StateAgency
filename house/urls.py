from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path('detail/<slug:slug>', views.PropertyDetailView.as_view(), name='detail_property'),
    path('all', views.PropertyListView.as_view(), name='list_property'),
    path('search', views.PropertySearchListView.as_view(), name='search_property'),
]
