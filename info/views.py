from django.shortcuts import render, HttpResponse


def main(request):
    return render(request, 'info/index.html', context={})


def check(request):
    return render(request, 'info/check.html', context={})
