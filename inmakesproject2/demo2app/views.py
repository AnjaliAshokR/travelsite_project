from django.http import HttpResponse
from django.shortcuts import render
from .models import places,travel_agents
# Create your views here.
def home(request):
    obj=places.objects.all()
    obj_agents=travel_agents.objects.all()
    return render(request, "index.html", {'result':obj, 'res_agents': obj_agents})
def register1(request):
    return HttpResponse("register here1")
# def operation(request):
#     return render(request,"about.html")
# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res_add=x+y
#     res_sub=x-y
#     res_div=x/y
#     res_mul=x*y
#     return render(request, "result.html", {'addition': res_add,'subtraction': res_sub, 'multiplication': res_mul,
#                                            'division': res_div, 'number1': x, 'number2': y})
# def contact(request):
#     return HttpResponse("Here is the contact")
# def details(request):
#     return render(request,"details.html")
# def thanks(request):
#     return HttpResponse("Thanks")