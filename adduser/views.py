from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from adduser.models import User
from adduser.forms import UserForm

def index(request):
    user_list = User.objects.all().order_by('last_name')
    context = {'user_list': user_list}
    return render(request, 'adduser/index.html', context)


def detail(request, user_id):
    userdetail = User.objects.get(pk=user_id)
    return render(request, 'adduser/detail.html', {'userdetail': userdetail})

def addnewuser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adduser')
    else:
        form = UserForm()

    return render(request, 'adduser/addnewuser.html', {'form': form})


def edituser(request, user_id):
    data = User.objects.get(pk=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adduser/'+user_id)
    else:
        form = UserForm(instance=data)
    return render(request, 'adduser/edituser.html', {'form': form})


def deluser(request, user_id):
    d = User.objects.get(pk=user_id)
    d.delete()
    return HttpResponseRedirect('/adduser')


