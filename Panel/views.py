from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.validators import validate_email
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required
def index(req):
    c = {"user": auth.get_user(req)}
    c.update({
        "active_menu": "Dashboard"
    })
    return render_to_response('user/panel/index.html', c)

@login_required
def logout(req):
    auth.logout(req)
    return HttpResponseRedirect('/accounts/login')

@login_required
def profile(req):
    message = ""
    active_menu = "Account"
    if req.POST:
        user = auth.get_user(req)
        if req.POST['jabber'] == user.email:
                message = {"text": "Nothing to update.", "color": "grey"}
        else:
            try:
                check_email = validate_email(req.POST['jabber'])
                message = {"text": "Success update.", "color": "green"}
                user.email = req.POST['jabber']
                user.save()
            except:
                message = {"text": "Error", "color": "red"}

    c = {"user": auth.get_user(req)}
    c.update(csrf(req))
    c.update({"message":message})
    c.update({"active_menu": active_menu})
    return render_to_response('user/panel/profile.html', c)