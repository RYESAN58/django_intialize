from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse




# Create your views here.
def root(request):
    return redirect("/blog")

def index(request):
    # return JsonResponse({"title": "My Blog", "content": "This is My blog"})
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, my_val):
    return HttpResponse(f" blog number {my_val}")

def edit(request, my_val):
    return HttpResponse(f" blog number to edit  {my_val}")

def desteoy(request, my_val):
    return redirect("/")

def jsonify(request):
    return JsonResponse({"title": "My Blog", "content": "This is My blog"})