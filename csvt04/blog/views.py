from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import Author,Book


def show_authors(req):
	authors = Author.objects.all()
	return render_to_response('show_authors.html',{'authors':authors})


def show_books(req):
	books = Book.objects.all()
	return render_to_response('show_books.html',{'books':books})



