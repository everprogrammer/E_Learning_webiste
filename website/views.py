from django.shortcuts import render
from .forms import ContactForm, NewsletterForm
from django.http import HttpResponse, HttpResponseRedirect

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
            return HttpResponse('done')
        else:
            return HttpResponse('Not valid')
        
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = NewsletterForm()
    return render(request, 'website/index.html', {'form': form})
        