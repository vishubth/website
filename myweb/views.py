from django.shortcuts import render
from .models import Contact
import requests, json


def index(request):
    r = requests.get('https://api.quotable.io/random')
    json_data = json.loads(r.text)
    quote = json_data.get('content')

    context = {'quotes': quote}
    return render(request, 'myweb/index.html', context)


def base(request):
    return render(request, 'myweb/base.html')


def portfolio(request):
    return render(request, 'myweb/portfolio.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(full_name=name, email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'myweb/thank.html')
    else:
        return render(request, 'myweb/contact.html')
