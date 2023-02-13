from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]

    questions = []
    replies = []

    for q in latest_question_list:
        entry = {}
        entry['question_id'] = q.id
        entry['question_text'] = q.question_text
        questions.append(entry)

        for r in q.get_choices():
            entry = {}
            entry['choice_id'] = r.id
            entry['choice_text'] = r.choice_text
            entry['votes'] = r.votes
            replies.append(entry)

    context = {
        'questions': questions,
        'replies': replies,
        }

    return render(request, 'index.html', context)

def castVote(request):    
    question_id = request.POST['question_id']
    choice_id = request.POST['choice_id']

    print(question_id, choice_id)


    question = Question.objects.get(pk=question_id)
    choice = question.get_choices().get(pk=choice_id)
    choice.votes += 1
    choice.save()
    
    return HttpResponse("Vote cast")