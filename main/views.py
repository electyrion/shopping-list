from django.shortcuts import render
from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Oberyn Martell',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)