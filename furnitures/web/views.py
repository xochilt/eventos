from django.shortcuts import render


from django.http import HttpResponse


import datetime

#def index(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s. In the furniture... :) </body></html>" % now
#    return HttpResponse(html)
def index(request):
    now = datetime.datetime.now()
    html = "Message from view furnitures"
    #return render(request, '/index.html',{'html':html})
    return render(request, 'index.html', {"html": "html"})

def furnitures(request):
    now = datetime.datetime.now()
    html = "Message from view furnitures"
    #return render(request, '/index.html',{'html':html})
    return render(request, 'index.html', {"html": "html"})

def about(request):
    now = datetime.datetime.now()
    html = "Message from view furnitures"
    #return render(request, '/index.html',{'html':html})
    return render(request, 'about.html', {"html": "html"})

def contact(request):
    now = datetime.datetime.now()
    html = "Message from view furnitures"
    #return render(request, '/index.html',{'html':html})
    return render(request, 'contact.html', {"html": "html"})

def blog(request):
    now = datetime.datetime.now()
    html = "Message from view furnitures"
    #return render(request, '/index.html',{'html':html})
    return render(request, 'blog.html', {"html": "html"})


from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded

def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))
    return TemplateResponse(request, 'payment.html', {'form': form, 'payment': payment})





