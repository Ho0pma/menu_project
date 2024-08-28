from django.shortcuts import render


def home(request):
    return render(request, 'menu/home.html')

def one(request):
    return render(request, 'menu/one.html')

def two(request):
    return render(request, 'menu/two.html')

def three(request):
    return render(request, 'menu/three.html')

def four(request):
    return render(request, 'menu/four.html')

def five(request):
    return render(request, 'menu/five.html')

def shelf_one(request):
    return render(request, 'menu/shelf_one.html')

def shelf_two(request):
    return render(request, 'menu/shelf_two.html')

def box_one(request):
    return render(request, 'menu/box_one.html')

def box_two(request):
    return render(request, 'menu/box_two.html')

def nails(request):
    return render(request, 'menu/nails.html')

def saw(request):
    return render(request, 'menu/saw.html')

def axe(request):
    return render(request, 'menu/axe.html')

def screws(request):
    return render(request, 'menu/screws.html')

def old_iron(request):
    return render(request, 'menu/old_iron.html')


