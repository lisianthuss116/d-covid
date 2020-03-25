from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime
import time
import json
import requests

from .services import *


def main(request):
    context = main_api(request=request)
    return render(request, 'index.html', context)


def as_card(request):
    limit = request.GET.get('limit')
    context = card_api(request=request, limit=limit)
    return render(request, 'as_card.html', context)


def detailed(request):
    context = detailed(request=request)
    return render(request, 'detailed.html', context)
