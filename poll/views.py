#coding:utf8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404
from models import Question,Choice
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'poll/index.html',context)
    # output = '<br>'.join([p.question_text for p in latest_question_list])
    # print type(output)
    # return HttpResponse('欢迎来到千峰在线投票!!!<hr>' + output.encode('utf-8'))

def detail(request,qid):
    question = get_object_or_404(Question,pk=qid)
    context = {'question' : question}
    return render(request,'poll/detail.html',context)

    # return HttpResponse('你正在投票详情页，投票id是%s' % str(qid))

def resuls(request,qid):
    # return HttpResponse('你正在投票结果页，投票id是%s' % str(qid))
    question = get_object_or_404(Question, pk=qid)
    return render(request,'poll/results.html',{'question':question})

def vote(request,qid):
    # return HttpResponse('你正在投票，投票id是%s' % str(qid))
    p = get_object_or_404(Question,pk=qid)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'poll/detail.html',{
            'question' : p,
            'error_message' : '请选择一个选项',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results',args=(qid,)))
