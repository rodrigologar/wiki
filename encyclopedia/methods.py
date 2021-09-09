import markdown2
from random import randint

from . import util

def mdConversion(title):
    page = util.get_entry(title)
    
    if not page:
        notFound = "<h1>Page not Found</h1>"
        
        return notFound
    
    html = markdown2.markdown(page)
    
    return html

def randomPageGenerator():
    max = len(util.list_entries())
    
    entry = randint(0, (max - 1))
    
    return entry