from django.shortcuts import render, redirect
from .forms import AppointmentForm

def home(request):
    return render(request, 'booking/home.html')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = AppointmentForm()
    return render(request, 'booking/book.html', {'form': form})

def success(request):
    return render(request, 'booking/success.html')