import markdown2
from random import randint

from . import util

def mdConversion(title):
    page = util.get_entry(title)
    
    if not page:
        notFound = "<h1>Page not Found</h1>"
        value = "Create Page"
        
        return {"html": notFound, "value": value}
    
    html = markdown2.markdown(page)
    value = "Edit"
    
    return {"html": html, "value": value}

def randomPageGenerator():
    max = len(util.list_entries())
    
    entry = randint(0, (max - 1))
    
    return entry