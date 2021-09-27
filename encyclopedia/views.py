from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django import forms
from django.http import HttpResponse

from . import methods
from . import util

def index(request):    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entries(request, title):
    if request.method == "POST":
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            "title": title,
            "content": content
        })
    
    return render(request, "encyclopedia/entries.html", {
        "title": title,
        "entry": methods.mdConversion(title)['html'],
        "value": methods.mdConversion(title)['value']
    })
    
def search(request):
    searched_entry = request.GET['q']
    
    if util.get_entry(searched_entry) != None:
        return render(request, "encyclopedia/entries.html", {
            "title": searched_entry,
            "entry": methods.mdConversion(searched_entry)['html'],
            "value": methods.mdConversion(searched_entry)['value']
        })
        
    else:
        entries = util.list_entries()
        results = []
        for entry in entries:
            if searched_entry in entry.lower():
                results.append(entry)
        
        return render(request, "encyclopedia/results.html", {
            "results": results
        })
        
def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("info")

        if util.get_entry(title) != None:
            return render(request, "encyclopedia/error.html", {
                "title": title
            })
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/entries.html", {
                "title": title,
                "entry": methods.mdConversion(title)['html'],
                "value": methods.mdConversion(title)['value']
            })
            
    return render(request, "encyclopedia/new_page.html")

def edit_page(request):
    title = request.GET["title"]
    content = request.GET["info"]
        
    util.save_entry(title, content)
        
    return render(request, "encyclopedia/entries.html", {
            "title": title,
            "entry": methods.mdConversion(title)['html'],
            "value": methods.mdConversion(title)['value']
    })
    
def random(request):
    entries = util.list_entries()
    index = methods.randomPageGenerator()
    random_entry = entries[index]
    
    return render(request, "encyclopedia/entries.html", {
        "title": random_entry,
        "entry": methods.mdConversion(random_entry)['html'],
        "value": methods.mdConversion(random_entry)['value']
    })