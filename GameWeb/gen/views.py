from django.shortcuts import render,get_object_or_404
from .models import Action,Aventure,Role,Sport

# Create your views here.
def home(request):
    return render(request,'gen/home.html')

def action(request):
    ac=Action.objects
    return render(request,'gen/action.html',{'action':ac})

def adventure(request):
    av=Aventure.objects
    return render(request,'gen/adventure.html',{'adventure':av})

def role(request):
    ro=Role.objects
    return render(request,'gen/role.html',{'role':ro})

def sport(request):
    sp=Sport.objects
    return render(request,'gen/sport.html',{'sport':sp})

def acdetail(request,action_id):
    ac_detail = get_object_or_404(Action, pk=action_id)
    return render(request, 'gen/adetail.html', {'action': ac_detail})

def avdetail(request,adventure_id):
    av_detail = get_object_or_404(Aventure, pk=adventure_id)
    return render(request, 'gen/avdetail.html', {'adventure': av_detail})

def roledetail(request,role_id):
    role_detail = get_object_or_404(Role, pk=role_id)
    return render(request, 'gen/roledetail.html', {'role': role_detail})

def sportdetail(request,sport_id):
    sport_detail = get_object_or_404(Sport, pk=sport_id)
    return render(request, 'gen/sportdetail.html', {'sport': sport_detail})


