from django.shortcuts import render
from django.http import HttpResponse, Http404
from polls.models import Poll, Choice
# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list':latest_poll_list,}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Exception:
        raise Http404
    return render(request, 'polls/detail.html', {'poll':poll})

def vote(request, poll_id):
    return HttpResponse("You are voting on poll%s."%poll_id)

def result(req, poll_id):
    return HttpResponse("You are looking at the result of poll %s."%poll_id)
    