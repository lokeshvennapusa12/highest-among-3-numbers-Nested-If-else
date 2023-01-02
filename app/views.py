from django.shortcuts import render

def nestedif(request):

    d={'a':20 , 'b':40 , 'c':10}

    return render(request,'nestedif.html',d)
