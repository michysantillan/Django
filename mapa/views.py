from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show(request):
	return HttpResponse("hola desde el cliente")

def login(request):
	nombre = 'Michy'
	context = { 'nombre': nombre}
	return render(request, 'login.html',context)