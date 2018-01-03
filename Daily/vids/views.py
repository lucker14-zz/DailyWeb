from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'vids/home.html')

def contact(request):
	return render(request, 'vids/contact.html', {'contact':['Chceš se nás na něco zeptat? Neváhej napsat na my@9roads.cz']})