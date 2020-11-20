from django.shortcuts import render
import requests

def get_main_page(request):
    url = 'http://127.0.0.1:8000/hello/'
    headers = {'Authorization': 'Token b537fe80957f00a54b515e8c356ebde6b61616a9'}
    r = requests.get(url, headers=headers)
    
    return render(request, 'main_page/index.html', context={'r': r.text})

