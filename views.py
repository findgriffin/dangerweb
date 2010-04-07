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
        quoteset = []
        for k in keys:
            models.Keyword.
        
        if len(list) == 0:
            return render_to_response('no_result.html')
        t = get_template('results.html')
        search_time = time.time() - start_time
        html = t.render(Context({'title': keys, 'content': list,'no_of_results': len(list),\
                'time_to_find': "%.2f" % search_time}))
        response = HttpResponse(html)
        return response
    else:
        return render_to_response('simpson.html')

def home(request):
    return render_to_response('simpson.html')

def vote(request):
    if request.session['has_voted']:
        return Null
    else:
        request.session['has_voted'] = True;

