from django.shortcuts import render

# Create your views here.
def forecast_main_page(request):
    return render(request, 'forecast/main.html')