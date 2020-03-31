from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import time
import json
import datetime
import requests


# endpoint
data_all = requests.get('https://corona.lmao.ninja/all')
data_by_country = requests.get('https://corona.lmao.ninja/countries/')


def main_api(request):
    fucking_list = ['updated', 'affectedcountries']

    datas_all = []
    for i, j in data_all.json().items():
        if str.lower(i) in fucking_list:
            pass
        else:
            datas_all.append({str.upper(i): j})

    # context
    context = {
        "datas": datas_all,
        "last_update": last_update()
    }
    return context


def card_api(request, limit=None):
    # paginate
    paginate_by = limit if limit is not None else 20
    paginator = Paginator(data_by_country.json(), paginate_by)
    page = request.GET.get('page')
    datas = paginator.get_page(page)

    # context
    context = {
        "total_data": data_all.json()['affectedCountries'],
        "last_update": last_update(),
        "datas": datas,
    }
    return context


def last_update():
    unix_timestamp = data_all.json()['updated']
    last_update = datetime.datetime.fromtimestamp(
        unix_timestamp//1000.0).strftime('%A, %B %d %Y, %H:%M:%S %p (UTC)')
    return last_update
