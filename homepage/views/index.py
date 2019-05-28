from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.core.mail import send_mail


@view_function
def process_request(request):

  

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print(name)
        print(email)
        print(message)

        
        # send_mail(
        #     '!!!Email From Portfolio!!!', ## Subject
        #     str(message), # Message content
        #     """${name} has sent you an email ---
        #         ${message}
        #     """,  # From email
        #     ['jordantroysmithson@gmail.com'], # To email
        #     fail_silently=False,
        # )
    

    utc_time = datetime.utcnow()
    context = {
        # sent to index.html:
        'utc_time': utc_time,
        # sent to index.html and index.js:
        jscontext('utc_epoch'): utc_time.timestamp(),
        
    }
    return request.dmp.render('index.html', context)