from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse


class UserFrom(forms.Form):
	name = forms.CharField()




def register(req):
	if req.method == 'POST':
		form = UserFrom(req.POST)
		if form.is_valid():
			print form.cleaned_data
			return HttpResponse('ok')
	else:
		form = UserFrom()
	return render_to_response('register.html',{'form':form})






