from django.shortcuts import render
from .models import StockMarketData

# Create your views here.

def home(request):
    # Fetch data from model
    data = StockMarketData.objects.all()

    # Pass the data to the template
    return render(request, 'home.html', {'data':data})