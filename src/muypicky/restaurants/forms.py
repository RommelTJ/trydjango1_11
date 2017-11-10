from django import forms

from .validators import validate_category
from .models import RestaurantLocation


class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name


class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

    def clean_location(self):
        location = self.cleaned_data.get("location")
        if location == "World":
            raise forms.ValidationError("Please be more specific")
        return location

