from django.shortcuts import render, get_object_or_404
from .models import Answer


def answer_list(request):
    answers = Answer.published.all()
    return render(request,
                  'ui_app/answer/answer_list.html', {'answers': answers})


def answer_detail(request, year, month, day, answer):
    answer = get_object_or_404(Answer, slug=answer,
                               status='published',
                               publish__year=year,
                               publish__month=month,
                               publish__day=day)
    return render(request,
                  'ui_app/answer/answer_detail.html', {'answer': answer})
