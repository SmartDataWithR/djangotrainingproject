from django.shortcuts import render
from search.models import Searchtitles
from django.http import HttpResponse
import json


def search(request):
    titles = Searchtitles.objects.all()
    titles_dict = {'title': titles}
    return render(request, "search.html", titles_dict)

def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Searchtitles.objects.filter(title__startswith=q)
        results = []
        print (q)
        for r in search_qs:
            results.append(r.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


