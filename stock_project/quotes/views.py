from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    # API Key: pk_bedfd3f917bf4d758890c03617cc4d01
    APITOKEN = "pk_bedfd3f917bf4d758890c03617cc4d01"
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_bedfd3f917bf4d758890c03617cc4d01")

    api = json.loads(api_request.content)
    #try:
    #    api = json.loads(api_request.symbol)
    #except Exception as e:
    #    api = "Error..."

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})