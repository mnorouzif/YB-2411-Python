from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'name',
            'email',
            'phone',
            'service',
            'appointment_date',
            'appointment_time'
        ]