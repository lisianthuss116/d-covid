from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime
import time
import json
import requests

from .services import *


def main(request):
    context = service_api(request=request)
    return render(request, 'index.html', context)
