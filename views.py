from django.shortcuts import render_to_response
from django.template import Template, Context
from django.template.loader import get_template
from django.http import Http404, HttpResponse
import libquote
def results(request):
    if 'q' in request.GET:
        keys = request.GET['q'].split()
        dbase = libquote.load_quoter('qlist.p','ind.p')
        qlist = dbase[0]
        ind = dbase[1]
        list = libquote.sort_results(libquote.or_search(keys,ind),keys)
        
        t = get_template('results.html')
        html = t.render(Context({'title': keys, 'content': list}))
        return HttpResponse(html)
    else:
        return render_to_response('simpson.html')

def home(request):
    return render_to_response('simpson.html')

def vote(request):
    errors = []
    if request.method == 'POST':
       qlist = libquote 
