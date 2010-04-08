from django.shortcuts import render_to_response
from django.template import Template, Context
from django.template.loader import get_template
from django.http import Http404, HttpResponse
import libquote
import time
import sys
import random
import simpsons.models as models

def results(request):
    if 'q' in request.GET:
        start_time = time.time()
        keys = request.GET['q'].split()
        quoteset = set()
        scores = dict()
        for k in keys:
            returned_keywords = models.Keyword.objects.filter(word=k).all()
            if len(returned_keywords) > 0:
                for qt in returned_keywords[0].quote_set.all():
                    quoteset.add(qt)
        if len(quoteset) == 0:
            return render_to_response('no_result.html')
        t = get_template('results.html')
        search_time = time.time() - start_time
        html = t.render(Context({'title': keys, 'content': quoteset,'scores': scores, 'no_of_results': len(quoteset),\
                'time_to_find': "%.2f" % search_time}))
        response = HttpResponse(html)
        return response
    else:
        return render_to_response('simpson.html')

def home(request):
    return render_to_response('simpson.html')

def vote(request):
    print request
    for key in request.POST:
        print key+": "+request.POST[key]
    return render_to_response('simpson.html')

def sort_qlist(qlist, keys):

    return None
