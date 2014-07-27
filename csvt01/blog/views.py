from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# from django.template import loader,Context
from django.shortcuts import render_to_response

# def index(req):
# 	t = loader.get_template('index1.html')
# 	c = Context({})

# 	return HttpResponse(t.render(c))

class Person(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex
	def say(self):
		return self.name


def index(req):
	user = {'name':'tom','age':22,'sex':'male'}
	# user = Person('lisa',22,'female')
	book_list = ['python','java','php','web']
	return render_to_response('index1.html',{'title':'pig','user':user,'book_list':book_list})


