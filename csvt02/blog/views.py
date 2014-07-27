from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Context,loader,Template
from django.shortcuts import render_to_response


def index(req):
	t = loader.get_template('index.html')
	c = Context({'uname':'alen'})
	return HttpResponse(t.render(c))

def index1(req):
	t = Template('<html><h1>hello {{uname}}</h1></html>')
	c = Context({'uname':'csvt'})
	return HttpResponse(t.render(c))

def index2(req):
	return render_to_response('index.html',{'uname':'csvt02'})