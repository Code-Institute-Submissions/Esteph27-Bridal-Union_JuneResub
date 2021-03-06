from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import BookingForm
from .models import Booking, CustomerProfile
from social_marketplace.models import Designer


@login_required
def booking(request, designer_id):
    '''
    a view to handle customer bookings
    '''

    user = request.user
    designer = Designer.objects.get(pk=designer_id)

    # get form info
    form = BookingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            customer_name = form.cleaned_data.get('customer_name')
            customer_email = form.cleaned_data.get('customer_email')
            designer_name = form.cleaned_data.get('designer_name')
            price_range = form.cleaned_data.get('price_range')
            date_of_wedding = form.cleaned_data.get('date_of_wedding')
            select_date = form.cleaned_data.get('select_date')
            select_time = form.cleaned_data.get('select_time')
            customer_message = form.cleaned_data.get('customer_message')
            BookingForm.save(form)
            messages.success(request, 'Thank you for booking. You can view the status of your booking in your account.')
    else:
        form = BookingForm()

    template = 'booking.html'
    context = {
        'form': form,
        'user': user,
        'designer': designer,
    }

    return render(request, template, context)


@login_required
def customer_profile(request):
    '''
    display customer's profile and bookings
    '''

    # get customer profile, otherwise create profile
    profile, created = CustomerProfile.objects.get_or_create(
        user=request.user,
    )

    bookings = profile.customer.all()

    template = 'customer_profile.html'
    context = {
        'profile': profile,
        'bookings': bookings,
    }

    return render(request, template, context)


@login_required
def edit_booking(request, booking_id):
    '''
    get customer booking and save changes
    '''

    get_booking = Booking.objects.get(pk=booking_id)
    form = BookingForm(request.POST or None, instance=get_booking)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your booking has been updated.')
        return redirect('customer_profile')

    template = 'edit_booking.html'

    context = {
        'get_booking': get_booking,
        'form': form,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def delete_booking(request, booking_id):
    '''
    Delete a customer booking
    '''

    booking = Booking.objects.get(pk=booking_id)
    booking.delete()
    messages.success(request, 'Your Booking has been canceled successfully!')
    return redirect('customer_profile')

