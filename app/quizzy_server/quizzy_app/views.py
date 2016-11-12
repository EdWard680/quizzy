#from django.shortcuts import render

## Create your views here.
#from django.http import HttpResponse


#def index(request):
    #return HttpResponse("Hello, world.")
    
from django.http import HttpResponse
from django.template import loader

#from .models import Question


def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('quizzy_app/index.html')
    context = {
        #'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))