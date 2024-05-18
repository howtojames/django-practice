from django.shortcuts import render
#add
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')

#second view
def help(request):
    dict = {'insert':'Help Page'}
    return render(request, "AppTwo/help.html", context=dict)


def users(request):
    user_list = User.objects.order_by("first_name")
    dict= {'user_list':user_list}
    return render(request, "AppTwo/users.html", context=dict)
