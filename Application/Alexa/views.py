from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
import alexa

@login_required
def index(req):
    c = {
        "title" : "Alexa Application",
        "active_menu": "Applications",
        "request": req,
        "user": auth.get_user(req)
    }
    if req.POST:
        category = req.POST['category']
        page_number = req.POST['page_number']
        try:
            if int(page_number) > 20: raise ValueError("Error")
            AlClass = alexa.Alexa()
            res = AlClass.getSitesByCategoryAndPageNumber(category, page_number)
            c.update({"results": res})
        except:
            c.update({
                "message": "Seem's there is error!"
            })

    c.update(csrf(req))
    return render_to_response('user/applications/alexa/index.html', c)