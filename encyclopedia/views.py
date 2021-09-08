from django.shortcuts import render
from django.http import HttpResponse

from . import methods
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entries(request, title):
    return render(request, "encyclopedia/entries.html", {
        "title": title,
        "entry": methods.mdConversion(title)
    })

