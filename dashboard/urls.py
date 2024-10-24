from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('alerts/', views.alerts, name='alerts'),
    path('list-of-medicines/', views.list_of_medicines, name='list-of-medicines'),
    path('sales-reports/', views.sales_reports, name='sales-reports'),
    path('stock-reports/', views.stock_reports, name='stock-reports'),
    path('predictions/', views.predictions, name='predictions'),
    path('drug-details/', views.drug_details, name='drug-details'),
    path('add-medicine/', views.add_medicine, name='add-medicine'),
    path('settings/', views.settings, name='settings'),
    path('stock-history/', views.stock_history, name='stock-history'),
]