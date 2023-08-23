from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    return render(request,'task/home.html'

                  )

def result(request):
    number1=int(request.GET.get('input1'))
    number2=int(request.GET.get('input2'))
    if request.GET.get('add')=="":
        ans=number1 +  number2
    elif request.GET.get('multiply')=="":
        ans=number1 * number2
    elif request.GET.get('divide')=="":
        ans=number1/number2
    else:
        ans=number1 - number2
    return render(request, 'task/result.html',
                  {'ans':ans}
                  )
