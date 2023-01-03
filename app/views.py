from django.shortcuts import render

# Create your views here.

def forloop(request):
    a={'abi':'abhi','a':[1,2,3,4,5,6,7]}
    return render(request,'forloop.html',a)

def loop(request):
    b={'jsp':'institution','brnch':'marathahalli'}
    return render(request,'loop.html',b)