from django.contrib import admin
from .models import Stock
# Register your models here.
#Step 1: import model
#Step2 :register model in admin area

admin.site.register(Stock)