import markdown2

from . import util

def mdConversion(title):
    page = util.get_entry(title)
    
    if not page:
        notFound = "<h1>Page not Found</h1>"
        
        return notFound
    
    html = markdown2.markdown(page)
    
    return html