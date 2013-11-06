from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.context_processors import csrf

def index(req):
    c = {}
    errors = []

    if req.POST:
        usernamereq = req.POST['username']
        passwordreq = req.POST['password']
        user = authenticate(username=usernamereq, password=passwordreq)

        if user is not None:
            login(req, user)
            c.update({"success": True})
        if user is None:
            errors.append("Invalid login or password.")

    c.update(csrf(req))
    c.update({"errors": errors})

    return render_to_response('user/login/index.html', c)