from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from adduser.models import User

def index(request):
    user_list = User.objects.all().order_by('last_name')
    context = {'user_list': user_list}
    return render(request, 'adduser/index.html', context)

def detail(request, user_id):
    userdetail = get_object_or_404(User, pk=user_id)
    return render(request, 'adduser/detail.html', {'userdetail': userdetail})


from adduser.forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

def addnewuser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            UserForm.save()
            return HttpResponseRedirect('index')
    else:
        form = UserForm()

    return render(request, 'adduser/addnewuser.html', {'form': form})


