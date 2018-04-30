from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.views.generic import ListView
from .models import Answer, TempPost


class AnswerListView(ListView):
    queryset = Answer.published.all()
    context_object_name = 'answers'
    template_name = 'ui_app/answer/answer_list.html'


def answer_list(request):
    answers = Answer.published.all()
    return render(request, 'ui_app/answer/answer_list.html', {'answers': answers})


def answer_detail(request, year, month, day, answer):
    answer = get_object_or_404(Answer, slug=answer,
                               status='published',
                               publish__year=year,
                               publish__month=month,
                               publish__day=day)
    return render(request,
                  'ui_app/answer/answer_detail.html', {'answer': answer})


# class TempPostListView(ListView):
#     queryset = TempPost.published.all()
#     context_object_name = 'tempposts'
#     template_name = 'ui_app/temppost/temppost_list.html'
#
#
# def temppost_list(request):
#     tempposts = TempPost.published.all
#     return render(request,
#                     'ui_app/temppost/temp post_list.html', {'tempposts': tempposts})


def temppost_list(request):
    tempposts = TempPost.objects.all()
    return TemplateResponse(request, 'ui_app/temppost/temppost_list.html', {'tempposts': tempposts})


