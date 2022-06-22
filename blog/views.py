from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


from blog.models import Question, Answer
from blog.forms import QuestionForm, AnswerForm

# Create your views here.



def index(request):
    question_list = Question.objects.all()
    return render(request, 'blog/question_list.html', {'question_list':question_list})
    #return HttpResponse('첫 방문')


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'blog/question_detail.html', {'question':question})



def write(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('blog:index')
        
    else:
        form = QuestionForm()

    return render(request, 'blog/question_write.html', {'form':form})




def modify(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('blog:detail', pk=pk)
        
    else:
        form = QuestionForm(instance=question)

    return render(request, 'blog/question_write.html', {'form':form})