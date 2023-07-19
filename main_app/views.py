from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

def index(request):
    return HttpResponse('<h1>Hello Andrew</h1>')

def data(request):
    with open('main_app/data/index.json', 'r') as file:
        req_data = json.load(file)
    return JsonResponse(req_data)
