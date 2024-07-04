from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('main/', views.main_page, name='main_page'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.registerPage, name='signup'),
    path('<str:stock_id>/', views.stock_detail, name='stock_detail'),
]
