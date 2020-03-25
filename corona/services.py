from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime
import time
import json
import requests


# api endpoint
data_by_country = requests.get('https://corona.lmao.ninja/countries/')
data_all = requests.get('https://corona.lmao.ninja/all')

def service_api(request):
    # varaibles
    datas_country = []
    datas_all = []
    paginate_by = 20

    # loop data by country
    for i in data_by_country.json():
        datas_country.append(i['country'])
    # loop data all
    for i, j in data_all.json().items():
        datas_all.append(j)


    # paginate
    paginator = Paginator(data_by_country.json(), paginate_by)
    page = request.GET.get('page')
    datas = paginator.get_page(page)

    # context
    context = {
        "total_data": len(datas_country),
        "data_all": datas_all,
        "datas_country": datas
    }
    return context
