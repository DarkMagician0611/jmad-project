from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Solo

# Create your views here.
def index(request):
	context = {'solos' : Solo.objects.filter(instrument=request.GET.get('instrument', None))}
	return render_to_response('solos/index.html', context)