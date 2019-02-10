from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from listings.views import house
from .forms import EnquiryForm, ContactForm
from .models import ContactMessage, PropertyEnquire


def send_contact_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            messages.success(request, "Thank you for your message!")
            return redirect('/#contact-us')
    else:
        return redirect('index')


@login_required
def send_enquire(request, user_id, house_id):
    if user_id is not int(request.session['_auth_user_id']):
        return redirect('index')
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your enquire has been send.")
            return house(request, house_id)
        else:
            messages.error(request, form.errors)
            return house(request, house_id)
    else:
        return redirect('index')


@login_required
def get_messages(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user_enquiries = PropertyEnquire.objects.filter(to_id=request.session['_auth_user_id'])
            data = serializers.serialize('json', user_enquiries)
            return HttpResponse(data)
        else:
            return redirect('index')
    else:
        return redirect('index')
