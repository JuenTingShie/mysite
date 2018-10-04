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
def menu(response):
    food1 = {'name':'番茄炒蛋',
            'price':60,
            'comment':'好吃',
            'spicy':False}
    food2 = {'name':'滑蛋雞肉飯',
            'price':85,
            'comment':'好香',
            'spicy':False}
    foods = [food1,food2]
    return render_to_response('menu.html',locals())