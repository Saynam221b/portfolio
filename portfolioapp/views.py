from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import UploadFileForm
from .utils import process_user_input_and_predict

# Create your views here.
def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def experience(request):
    return render(request, 'experience.html')

def contact(request):
    return render (request, 'contact.html')

def upload(request):
    return render (request, 'upload.html')


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


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            age = int(request.POST.get('age'))
            gender = int(request.POST.get('gender'))
            csv_file = request.FILES['csv_file']  # Get the uploaded CSV file
            
            predictions = process_user_input_and_predict(age, gender, csv_file)
            return render(request, 'results.html', {'predictions': predictions})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})