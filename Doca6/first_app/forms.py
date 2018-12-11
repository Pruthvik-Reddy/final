from django import forms
from first_app.models import Appointments
from doc_app.models import slots
from django.core import validators
from django.core.exceptions import ValidationError

SLOT_CHOICES=[
    ('slot1','9:00 Am'),
('slot2','3:00 Pm'),
('slot3','7:00 Pm'),
]

class FormName(forms.Form):
    loc=forms.CharField()
    cat=forms.CharField()

#class slotform(forms.Form):
#    slot = forms.CharField(label="Choose Slot", widget=forms.Select(choices=SLOT_CHOICES))

class AppForm(forms.Form):
    doc_name = forms.CharField(max_length=30)
    fees = forms.IntegerField()
    rating = forms.IntegerField()
    date=forms.DateField()
    #slot=forms.CharField()
class Form2(forms.Form):
    doc_name=forms.CharField(max_length=30)

    date=forms.DateField()
   # start_time=forms.CharField(validators=[check_slot()])
    start_time=forms.CharField()
    """
    def clean(self):
        if Appointments.objects.filter(doc_name=self.doc_name,fees=self.fees,start_time=self.start_time).count() >= 2:
            raise ValidationError('The Slot Is full!Please Book a different Slot!')
    """