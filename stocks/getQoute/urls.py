from django.urls import path
from . import views
 
urlpatterns = [
	path('', views.home,name = "home"), #We dont want the url to be anything	
	path('about', views.about,name = "about"),
	path('add_stock.html',views.add_stock,name = "add_stock"),
	path('delete_stocks/<stock_id>',views.delete_stocks,name = "delete"),
	path('delete_stock.html',views.delete_stock,name="delete_stock"),
]