from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'sapan/home.html', context=context)