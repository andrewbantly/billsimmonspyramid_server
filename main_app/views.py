from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .import_data import read_json_files
import json

def index(request):
    return HttpResponse('<h1>Hello Andrew</h1>')

def data(request):
    print("request:")
    print(request)
    print("  ")
    with open('main_app/data/index.json', 'r') as file:
        req_data = json.load(file)
    return JsonResponse(req_data)
