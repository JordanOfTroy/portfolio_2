from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from homepage import models as cmod


class NameForm(forms.Form):
    first_name_yo = forms.CharField(label='first name', max_length=30)
    last_name = forms.CharField(label='last name', max_length=30)

@view_function
def process_request(request):

    form = NameForm()

    if request.method == 'POST':
        if form.is_valid():
            u = cmod.Person()
            u.first_name_yo = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
    

    utc_time = datetime.utcnow()
    context = {
        # sent to index.html:
        'utc_time': utc_time,
        # sent to index.html and index.js:
        jscontext('utc_epoch'): utc_time.timestamp(),
        'form': form
    }
    return request.dmp.render('index.html', context)