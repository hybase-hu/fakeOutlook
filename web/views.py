from django.shortcuts import render

from web.forms import LoginForm


# Create your views here.
def login(request):
    login_form = LoginForm()
    context = {'form':login_form}
    template = "web/login.html"
    return render(request,template,context)