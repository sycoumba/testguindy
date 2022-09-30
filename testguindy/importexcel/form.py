from django import forms
from .models import Categories

class PersonData(forms.Form):
	class meta:
		model = Categories
		fields = '__all__'