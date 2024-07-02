from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('main/', views.main_page, name='main_page'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.registerPage, name='signup'),
    path('<str:stock_id>/', views.stock_detail, name='stock_detail'),
    # path('<str:stock_id>/<str:view_type>/', views.chart_view, name='chart_view'),
    # path('detail/<str:stock_id>/', views.detail_page, name='detail'),
    # path('api/<str:stock_id>/monthly/', views.get_monthly_data, name='api-monthly-data'),
    # path('api/<str:stock_id>/average/', views.get_average_data, name='api-average-data'),
]