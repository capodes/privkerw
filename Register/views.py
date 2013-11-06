from django.core.validators import validate_email
from django.core.validators import ValidationError
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

def index(req):
    c = {}
    c.update(csrf(req))
    errors = []
    ### Process request.
    if req.POST:
        try:
            ### First input validation
            jabber_error = validate_email(req.POST['jabber'])
            if req.POST['username'] == '': raise ValidationError(message="Enter valid username.")
            if req.POST['password'] == '': raise ValidationError(message="Enter valid password.")
            ### Second validation - in database
            if User.objects.filter(username__exact=req.POST['username']).count() > 0:
                errors.append("Already in our database.")
                raise ValidationError(message="Already in our database.")
        except ValidationError as Errors:
            errors.append("Please accurately fill the fields!")

        c.update({'errors':errors})
        c.update({'request':req.POST})

        if len(errors)==0:
            user = User.objects.create_user(req.POST['username'], req.POST['jabber'], req.POST['password'])
            user.save()

            c.update({'errors':['Successfully registered!']})

    return render_to_response('user/register/index.html', c)