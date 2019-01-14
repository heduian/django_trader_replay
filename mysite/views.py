from django.shortcuts import render
from django.http import HttpResponse
from .models import GBP_m15
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def main(request):
	return render(request, 'farm/farm_data.html')

@csrf_exempt
def show_data(request):
    if request.method == 'POST':
        year = request.POST.get("year")
        farmdatas = GBP_m15.objects.filter(date=year)
        return render(request,'farm/echarts_data.html', {"farmdatas":farmdatas})

