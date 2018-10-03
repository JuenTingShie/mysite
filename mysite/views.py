from django.shortcuts import render_to_response
from django.http import HttpResponse
def here(request):
	return HttpResponse('I am here')
def math(request,a,b):
	s = a+b
	d = a-b
	p = a*b
	q = a/b
	return render_to_response('math.html',locals())