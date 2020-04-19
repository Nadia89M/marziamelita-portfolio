from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from photos.models import Photo
from contact.forms import ContactForm


def index(request):
    photos = Photo.objects.all().order_by('id').reverse()[:3]
    context = {
        'photos': photos,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html', {})


def thanks(request):
    return render(request, 'pages/thanks.html', {})


def services(request):
    return render(request, 'pages/services.html', {})


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # Send email
            send_mail(
                'Contact Inquiry',
                'There has been an inquiry. Sign into the admin panel for more info.',
                'marziauk22@gmail.com',
                ['marziauk22@gmail.com'],
            )
            return thanks(request)

    return render(request, 'pages/contact.html', {'form': form})
