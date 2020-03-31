from django.shortcuts import render
from .services import *


def main(request):
    try:
        context = main_api(request=request)
        return render(request, 'index.html', context)
    except:
        return render(request, 'handler/internal_err.html')


def as_card(request):
    try:
        limit = request.GET.get('limit')
        context = card_api(request=request, limit=limit)
        return render(request, 'as_card.html', context)
    except:
        return render(request, 'handler/internal_err.html')


def detailed(request):
    context = detailed(request=request)
    return render(request, 'detailed.html', context)
