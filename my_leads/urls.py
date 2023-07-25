from django.urls import path
from .import views
from .views import LeadListCreateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.main, name="home"),
    path('leads/', LeadListCreateView.as_view(), name='lead-list-create'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]

