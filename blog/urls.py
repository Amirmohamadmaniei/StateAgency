from django.urls import path
from blog import views


app_name = 'blog'


urlpatterns = [
    path('detail/<slug:slug>', views.BlogDetailView.as_view(), name='detail_blog'),
    path('all', views.BlogListView.as_view(), name='list_blog'),
]