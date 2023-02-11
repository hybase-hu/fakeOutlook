from django.shortcuts import redirect


def bad_request(request,exception):
    return redirect("/")