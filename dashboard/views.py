from django.shortcuts import render

from .models import Blackcoffer
from .forms import BlackcofferForm
# Create your views here.


# def blackcoffer(request):
#     details = Blackcoffer.objects.all()
    
#     context = {
#         'details': details,
#     }
#     return render(request, 'page/details_list.html', context)


def index(request):
    total_data = Blackcoffer.objects.all()
    intensity = Blackcoffer.objects.values('intensity'),
    likelihood = Blackcoffer.objects.values('likelihood'),
    relevance = Blackcoffer.objects.values('relevance'),
    start_year = Blackcoffer.objects.values('start_year'),
    country = Blackcoffer.objects.values('country'),
    topic = Blackcoffer.objects.values('topic'),
    region = Blackcoffer.objects.values('region'),
    
    all_items = [intensity, likelihood, relevance, start_year, country,topic, region]
   
    context = {
        "intensity":intensity,
        "likelihood":likelihood,
        "relevance":relevance,
        "start_year":start_year,
        "country":country,
        "topic":topic,
        "region":region,
        "all_items": all_items,
        "total_data":total_data,
        
    }
    return render(request, 'dashboard/index.html', context)