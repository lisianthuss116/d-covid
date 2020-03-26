from django.shortcuts import render
from .services import ApiService


def main(request):
    context = ApiService.main_api(request=request)
    return render(request, 'index.html', context)


def as_card(request):
    limit = request.GET.get('limit')
    context = ApiService.card_api(request=request, limit=limit)
    return render(request, 'as_card.html', context)


def detailed(request):
    context = ApiService.detailed(request=request)
    return render(request, 'detailed.html', context)
