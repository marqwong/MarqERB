from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Contact  

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing_title = request.POST['listing_title']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_connected = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_connected:
                messages.error(request, "You already have been made an inquiry for this listing.")
                return redirect("/listings/" + listing_id)
        contact = Contact(
            listing=listing_title,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )
        contact.save()

        messages.success(request, "Your request has been submitted. The realtor will get back to you soon.")
    return redirect("/listings/" + listing_id)

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, 'Your profile has been updated successfully!')
    return redirect('dashboard')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted successfully!')
        return redirect('index')
    return redirect('dashboard')