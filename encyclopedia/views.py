from django.http import request
from django.shortcuts import redirect, render
from django import forms

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
    
def search(request):
    searched_entry = request.GET['q']
    
    if util.get_entry(searched_entry) != None:
        return render(request, "encyclopedia/entries.html", {
            "title":searched_entry,
            "entry":methods.mdConversion(searched_entry)
        })
        
    else:
        entries = util.list_entries()
        results = []
        for entry in entries:
            if searched_entry in entry.lower():
                results.append(entry)
        
        return render(request, "encyclopedia/results.html", {
            "results":results
        })
        
def new_page(request):
    return render(request, "encyclopedia/new_page.html")

