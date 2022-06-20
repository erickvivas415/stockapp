from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

# Create your views here.
def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        # API Key: pk_bedfd3f917bf4d758890c03617cc4d01
        APITOKEN = "pk_bedfd3f917bf4d758890c03617cc4d01"
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_bedfd3f917bf4d758890c03617cc4d01")
        api_news_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/news?token=pk_bedfd3f917bf4d758890c03617cc4d01")
        #api = json.loads(api_request.content)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        try:
            api_news = json.loads(api_news_request.content)
        except Exception as e:
            api_news = "Error..."

    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol above..."})

    return render(request, 'home.html', {'api': api, 'api_news': api_news})

def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json
    if request.method == 'POST':
        #ticker = request.POST['ticker'] this is a string. We need to pass a dictionary
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been added")
            return redirect('add_stock')
    else:
        ticker= Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_bedfd3f917bf4d758890c03617cc4d01")

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."

        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete_stock(request, stock_id):
    item = Stock.objects.filter(ticker= stock_id)
    item.delete()
    messages.success(request, "Stock has been deleted")
    return redirect('add_stock')