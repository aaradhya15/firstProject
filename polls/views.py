# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render,get_object_or_404

#from django.template import loader


def index(request):
	latestQuestionList = Question.objects.order_by('-pub_date')[:4]
	#template = loader.get_template('polls/index.html')
	context = {
		'latestQuestionList':latestQuestionList,
	}
	#return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)


