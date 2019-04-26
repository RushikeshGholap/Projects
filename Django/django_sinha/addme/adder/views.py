from django.shortcuts import render
from django.http import HttpResponse
from adder.models import numbers

# Create your views here.


#first time page
def index(request):
	return render(request, 'index.html')

#second time page after submit (with result)

def output(request):
	if request.method == 'POST':
		nums = numbers()
		nums.a = int(request.POST.get('a'))
		nums.b = int(request.POST.get('b'))
		nums.result = nums.a + nums.b

		nums.save()

		allnumbs = numbers()

		return render(request, 'index.html', {'result': nums.result, 'numbers': allnumbs.__class__.objects.all()})

	else:
		return render(request, 'index.html')