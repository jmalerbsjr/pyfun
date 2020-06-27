from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader



def index(request):
    template = loader.get_template("index.html")

    return HttpResponse(template.render())

def login(request):
    template = loader.get_template("login.html")

    return HttpResponse(template.render())

def search(request):
    template = loader.get_template("search.html")
    type = request.GET['type']

    if type == 'hotels':
        search_results = {"Hilton Inn": "Address 1",
                          "Four Points": "Address 2",
                          "Radisson": "Address 3",
                          "Travelodge": "Address 4"}
    if type == 'cars':
        search_results = {"Audi": "Address 1",
                          "Mercedes": "Address 2",
                          "Bentley": "Address 3"}

    data = search_results

    return HttpResponse(template.render({"data": data, "type": type}))

