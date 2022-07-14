from django import forms
from myApp.models import Order


class InterestForm(forms.Form):
    interested = forms.RadioSelect()
    levels = forms.IntegerField(min_value=1, max_value=10, initial=1)
    comments = forms.Textarea

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {
            'student': forms.RadioSelect,
            'order_date': forms.SelectDateWidget
        }

