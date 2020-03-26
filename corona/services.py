from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import time
import json
import requests


# endpoint
data_all = requests.get('https://corona.lmao.ninja/all')
data_by_country = requests.get('https://corona.lmao.ninja/countries/')


def main_api(request):
    datas_all = []
    total_data = countries(request=request)
    for i, j in data_all.json().items():
        datas_all.append({str.upper(i): j})

    # context
    context = {
        "total_data": len(total_data),
        "datas": datas_all[:3],
        "last_update": last_update()
    }
    return context


def card_api(request, limit=None):
    total_data = countries(request=request)

    # paginate
    if limit is not None:
        paginate_by = limit
    else:
        paginate_by = 20
    paginator = Paginator(data_by_country.json(), paginate_by)
    page = request.GET.get('page')
    datas = paginator.get_page(page)

    # context
    context = {
        "total_data": len(total_data),
        "last_update": last_update(),
        "datas": datas,
    }
    return context


def countries(request):
    # variables
    datas_country = []
    for i in data_by_country.json():
        datas_country.append(i['country'])

    return datas_country


def last_update():
    datas_all = []
    for i, j in data_all.json().items():
        datas_all.append({str.upper(i): j})

    update_time = int(datas_all[-1]['UPDATED'])
    now = int(round(time.time() * 1000))
    last_update = now - update_time

    sec, a = divmod(last_update, 1000)
    minute, b = divmod(sec, 60)
    hour, c = divmod(minute, 60)
    day, d = divmod(hour, 24)
    week, e = divmod(day, 7)
    if minute == 0:
        return f"{sec} seconds"
    elif hour == 0:
        return f"{minute} minute"
    elif day == 0:
        return f"{hour} hour"
    elif week == 0:
        return f"{day} day"
    else:
        return f"{week} week"
