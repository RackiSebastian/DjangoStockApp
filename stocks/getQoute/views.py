from django.shortcuts import render,redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm
# Create your views here.
#pk_bd24d698c2f24da5aefca0f43682d5ea

def home(request):
	import requests
	import json
	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_bd24d698c2f24da5aefca0f43682d5ea") #pass in url to api 
		try:
			api = json.loads(api_request.content)
		except:
			api = "Error check your ticker"
		return render(request,'home.html',{'api':api})

	else:
		return render(request,'home.html',{'ticker':'Enter a ticker symbol above'})  





def about(request):
	return render(request,'about.html',{})


def add_stock(request):
	#switching it up and using forms system
	'''if request.method == 'POST':
		ticker = request.POST['ticker']'''

	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request,("Stock added to your database"))
			return redirect('add_stock') 

	else:

		#pulling stuff out of databse v 
		ticker = Stock.objects.all()
		output = [] 
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+str(ticker_item)+"/quote?token=pk_bd24d698c2f24da5aefca0f43682d5ea")
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except:
				api = "Error check your ticker"
		return render(request,'add_stock.html',{'ticker':ticker,'output':output})

def delete_stocks(request,stock_id):
	item = Stock.objects.get(pk= stock_id) #primnary key is going to be stock id
	item.delete()
	messages.success(request,("Stock has been deleted"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request,'delete_stock.html',{'ticker':ticker})