from django.shortcuts import render
from django.http import HttpResponse
from adduser.models import User

def index(request):
    user_list = User.objects.all()
    return render(request, 'adduser/index.html', user_list)

def detail(request, user_id):
    return HttpResponse("You're looking at the details for %s." %user_id)


