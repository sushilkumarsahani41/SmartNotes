from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "welcome.html", {'today': datetime.datetime.today()})


@login_required(login_url="/admin")
def auth(request):
    return render(request, "auth.html",{})
