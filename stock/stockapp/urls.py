from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.registerPage, name='signup'),
]
