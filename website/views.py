from django.shortcuts import render
from .forms import ContactForm, NewsletterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')

def test_view(request):
    return render(request, 'website/test.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your ticket is submitted successfully!')
            return HttpResponseRedirect('/contact')
        else:
            messages.add_message(request, messages.ERROR,
                                 'An error occurred while submitting ticket!')
            return HttpResponseRedirect('/')
        
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'You have successfully subscribed to our newsletter!')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                                 'An error occurred while subscribing!')
            return HttpResponseRedirect('/')

    form = NewsletterForm()
    return render(request, 'website/index.html', {'form': form})
        

def handle_404(request, exception):
    return render(request, '404.html')