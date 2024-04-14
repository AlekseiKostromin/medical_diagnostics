from datetime import date

from django import forms
from .models import LabTest, TestCategory, Doctor, Booking


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LabTestForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ('name', 'category', 'description', 'price', 'time')


class DoctorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('specialization', 'category', 'price')


class TestCategoryForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = TestCategory
        fields = '__all__'


class BookingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('doctor', 'date', 'timeslot')

    def clean_date(self):
        day = self.cleaned_data['date']

        if day <= date.today():
            raise forms.ValidationError(
                'Выберите, пожалуйста, '
                'дату в будущем (завтра или позднее)',
                code='invalid'
            )
        return day
