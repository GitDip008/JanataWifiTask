from django.shortcuts import render, get_object_or_404
from .models import StockMarketData, SQLSMData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db.models import Q
import json
from django.core.paginator import Paginator

# Create your views here.

# # For JSON Model

# def home(request):
#     # Fetch data from model
#     data = StockMarketData.objects.all()
#
#     # Pass the data to the template
#     return render(request, 'home.html', {'data':data})
#


# For SQL MODEL
def index(request):
    datas = SQLSMData.objects.all().order_by('date')
    query = ""
    items_per_page = 50
    paginator = Paginator(datas, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    # Extracting and formatting data for the chart
    # sorted_dates = [data.date for data in datas]
    limited_data = page_obj.object_list
    sorted_dates = [data.date.strftime('%Y-%m-%d') for data in limited_data]  # Convert date objects to strings
    close_values = [float(data.close) for data in limited_data]
    # volume_values = [int(data.volume.replace(',', '')) for data in datas]

    # Remove commas from the string representation of volume (if it's a string)
    volume_values = [int(str(data.volume).replace(',', '')) if isinstance(data.volume, str) else int(data.volume) for
                     data in limited_data]


    if request.method == "POST":
        if "add" in request.POST:
            date = request.POST.get("date")
            trade_code = request.POST.get("trade_code")
            high = request.POST.get("high")
            low = request.POST.get("low")
            open = request.POST.get("open")
            close = request.POST.get("close")
            volume = request.POST.get("volume")

            SQLSMData.objects.create(
                date=date,
                trade_code = trade_code,
                high = high,
                low = low,
                open = open,
                close = close,
                volume = volume
            )
            messages.success(request, "Data added successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            date = request.POST.get("date")
            trade_code = request.POST.get("trade_code")
            high = request.POST.get("high")
            low = request.POST.get("low")
            open = request.POST.get("open")
            close = request.POST.get("close")
            volume = request.POST.get("volume")

            update_data = SQLSMData.objects.get(id=id)
            update_data.date = date
            update_data.trade_code = trade_code
            update_data.high = high
            update_data.low = low
            update_data.open = open
            update_data.close = close
            update_data.volume = volume

            update_data.save()

            messages.success(request, "Data Updated Successfully")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            SQLSMData.objects.get(id=id).delete()

            messages.success(request, "Data Deleted Successfully.")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            # datas = SQLSMData.objects.filter(Q(date__icontains=query) | Q(trade_code__icontains=query) | Q(high__icontains=query) | Q(low__icontains=query) | Q(open__icontains=query) | Q(close__icontains=query) | Q(close__icontains=query))
            datas = SQLSMData.objects.filter(Q(trade_code__icontains=query))

            sorted_dates = [data.date.strftime('%Y-%m-%d') for data in datas]  # Convert date objects to strings
            close_values = [float(data.close) for data in datas]
            # volume_values = [int(data.volume.replace(',', '')) for data in datas]

            # Remove commas from the string representation of volume (if it's a string)
            volume_values = [
                int(str(data.volume).replace(',', '')) if isinstance(data.volume, str) else int(data.volume) for
                data in datas]




    context = {"datas": datas, "query":query, 'sorted_dates': json.dumps(sorted_dates),
                                                'close_values': json.dumps(close_values),
                                                'volume_values': json.dumps(volume_values),
                                                'page_obj': page_obj}
    # datas = SQLSMData.objects.all()[:10]


    return render(request, "index.html", context=context)