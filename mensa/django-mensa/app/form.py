from django import forms
from django.forms.widgets import SelectDateWidget
from django.forms import ModelForm
from .models import Plates, MenuChoice, Employee, weekdays,Day
from django.contrib.auth.models import User, Group
#from parsley.decorators import parsleyfy
from datetime import date
import calendar

#@parsleyfy
class PlateForm(ModelForm):
        class Meta:
            model = Plates
            fields = ["name","price","menu_name"]
            #parsley_extras = {
            #    'price': {
            #        'min': "0",
            #        'error-message': "Non puoi inserire un prezzo negativo",
            #    },
            #}

        def save(self, commit=True):
            plate = super(PlateForm, self).save(commit=False)

            if commit:
                plate.save()
            return plate


class MenuForm(forms.Form):
    plate =  forms.ModelChoiceField(queryset = Plates.objects.filter(is_menu=False))




class OrdineForm(ModelForm):
    date = forms.ModelChoiceField(queryset= Day.objects.filter(id__gte = weekdays(calendar.day_name[date.today().weekday()])))
    #date = forms.ModelChoiceField(queryset=Day.objects.filter(id__gte = Day.objects.filter(d=calendar.day_name[date.today().weekday()]).first().id))
    plate_chosen = forms.ModelMultipleChoiceField(
                       widget = forms.CheckboxSelectMultiple,
                       queryset = Plates.objects.filter(is_menu=True))

    class Meta:
        model = Employee
        fields = ["date","plate_chosen"]
