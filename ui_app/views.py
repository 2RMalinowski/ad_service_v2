from django.shortcuts import render, get_object_or_404
from .models import Answer


def answer_list(request):
    answers = Answer.published.all()
    return render(request,
                  'ui_app/answer.html', {'answers': answers})


def answer_detail(request, year, month, day, post):
    answer = get_object_or_404(Answer, slug=post, status='published', publish__year=year,
                               publish__month=month, publish__day=day)
    return render(request,
                  'ui_app/detail.html', {'answer': answer})
