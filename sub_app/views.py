from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Answer


class AnswerListView(ListView):
    queryset = Answer.published.all()
    context_object_name = 'answers'
    template_name = 'sub_app/answer/answer_list.html'


def answer_list(request):
    answers = Answer.published.all()
    return render(request,
                  'sub_app/answer/answer_list.html', {'answers': answers})


def answer_detail(request, year, month, day, answer):
    answer = get_object_or_404(Answer, slug=answer,
                               status='published',
                               publish__year=year,
                               publish__month=month,
                               publish__day=day)
    return render(request,
                  'sub_app/answer/answer_detail.html', {'answer': answer})


