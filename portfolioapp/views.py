from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def experience(request):
    return render(request, 'experience.html')

def contact(request):
    return render (request, 'contact.html')



def contact_me(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('textarea')

        # Send email
        subject = 'New Contact Form Submission'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

        return render(request, 'contact.html')

    return render(request, 'contact.html')
