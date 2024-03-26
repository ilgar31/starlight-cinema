from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def order(request, amount):
    return render(request, 'order.html', {"amount": amount})
