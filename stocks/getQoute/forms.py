from django import forms 
from .models import Stock 

class StockForm(forms.ModelForm):
	class Meta: 
		model = Stock #our model that we are working on 
		fields = ["ticker"] #all the fields we will be saving 