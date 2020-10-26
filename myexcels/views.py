from django.shortcuts import render
from django.http import HttpResponse,Http404
#from django.template import loader
# Create your views here.


def index(request):
	#template = loader.get_template('myexcels/index.html')
	#return HttpResponse(template.render())
	formula = request.GET['formula']
	result = eval(formula, {})
	return HttpResponse(result)
	return render(request,'myexcels/index.html')
