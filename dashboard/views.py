from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Customer, Sale, Product, Order

def dashboard(request):
    context = {
        'total_customers': Customer.objects.count(),
        'total_sales': Sale.objects.count(),
        'total_profit': Sale.objects.aggregate(Sum('amount'))['amount__sum'],
        'out_of_stock': Product.objects.filter(stock=0).count(),
        'recent_orders': Order.objects.order_by('-id')[:5],
        'monthly_sales': Sale.objects.values('date__month').annotate(total=Sum('amount')).order_by('date__month'),
    }
    return render(request, 'dashboard/dashboard.html', context)

def inventory(request):
    return render(request, 'dashboard/inventory.html')

def alerts(request):
    return render(request, 'dashboard/alerts.html')

def list_of_medicines(request):
    return render(request, 'dashboard/list-of-medicines.html')

def sales_reports(request):
    return render(request, 'dashboard/sales-reports.html')

def stock_reports(request):
    return render(request, 'dashboard/stock-reports.html')

def predictions(request):
    return render(request, 'dashboard/predictions.html')

def drug_details(request):
    return render(request, 'dashboard/drug-details.html')

def add_medicine(request):
    return render(request, 'dashboard/add-medicine.html')

def settings(request):
    return render(request, 'dashboard/settings.html')
