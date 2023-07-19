from django.shortcuts import render
from django.http import HttpResponse
# from .import_data import read_json_files
import json

def index(request):
    return HttpResponse('<h1>Hello Andrew</h1>')

def data(request):
    # Call the function to read JSON files
    # json_data = read_json_files()
    with open('main_app/data/index.json', 'r') as file:
        req_data = json.load(file)
    # return render(req_data)
    return json(req_data)
    # return render(json_data)