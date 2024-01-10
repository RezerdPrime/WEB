from django.http import HttpResponse
from django.shortcuts import render

def articles_test(request):
    #return HttpResponse('<h1 style="color:red">Meine Leben ist vorbei</h1>')
    return render(request, 'articles/qz.html')

def ToPD(request):
    #return HttpResponse('<h1 style="color:red">Meine Leben ist vorbei</h1>')
    return render(request, 'articles/ToPD.html')