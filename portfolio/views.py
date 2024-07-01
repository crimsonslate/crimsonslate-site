from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Home",
        "company": settings.COMPANY,
    }
    return render(request, "portfolio/index.html", context=context)
