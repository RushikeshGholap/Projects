from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import *

# Create your views here.

def index(request):
	if request.method=='POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = DocumentForm()
		return render(request, 'index.html', {'form': form})