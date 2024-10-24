from django.shortcuts import render
from django.db.models import Sum, Count
from django.utils.translation import get_language
from .models import Customer, Sale, Product, Order
from utils.getWeatherContext import getWeatherContext,get_weather

def dashboard(request):
    context = getWeatherContext()

    context.update({
        'total_customers': Customer.objects.count(),
        'total_sales': Sale.objects.count(),
        'total_profit': 145000,
        'out_of_stock': Product.objects.filter(stock=0).count(),
        'recent_orders': Order.objects.order_by('-id')[:5],
        'monthly_sales': Sale.objects.values('date__month').annotate(total=Sum('amount')).order_by('date__month'),
    })
    return render(request, 'dashboard/dashboard.html', context)

def your_view(request):
    current_language = get_language()
    weather = get_weather(city, api_key, lang=current_language)

def inventory(request):
    context = getWeatherContext()
    return render(request, 'dashboard/inventory.html', context)

def alerts(request):
    context = getWeatherContext()
    return render(request, 'dashboard/alerts.html', context)

def list_of_medicines(request):
    context = getWeatherContext()
    return render(request, 'dashboard/list-of-medicines.html', context)

def sales_reports(request):
    context = getWeatherContext()
    return render(request, 'dashboard/sales-reports.html', context)

def stock_reports(request):
    context = getWeatherContext()
    return render(request, 'dashboard/stock-reports.html', context)

def predictions(request):
    context = getWeatherContext()
    return render(request, 'dashboard/predictions.html', context)

def drug_details(request):
    context = getWeatherContext()
    return render(request, 'dashboard/drug-details.html', context)

def add_medicine(request):
    context = getWeatherContext()
    return render(request, 'dashboard/add-medicine.html', context)

def settings(request):
    context = getWeatherContext()
    return render(request, 'dashboard/settings.html', context)

def stock_history(request):
    context = getWeatherContext()
    return render(request, 'dashboard/stock-history.html', context)
