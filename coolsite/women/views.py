from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect


def index(request):
    return HttpResponse("Страница приложения woman")


def categories(request, catId):
    if (request.GET):
        print(request.GET)

    if (request.POST):
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catId}</p>")


def archive(request, year):
    if (int(year) > 2023):
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена - 404</h1>")
