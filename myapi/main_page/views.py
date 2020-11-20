from django.shortcuts import render


def get_main_page(request):
    
    return render(request, 'main_page/index.html')

