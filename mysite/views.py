from django.shortcuts import render
from .models import Comment
from django.http import HttpResponseRedirect
from .forms import CommentForms
from django.core.mail import send_mail
# Create your views here.
def home_view(request):
    return render(request,'base.html')

def work_view(request):
    return render(request, 'work.html')

def skill_view(request):
    return render(request, 'skill.html')

def comment_view(request):
    return render(request, 'comment.html')

def comment_create(request):
    form = CommentForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = CommentForms()
    return render(request, 'sent.html')





#def send(request):
    #new_comment = request.POST.get('comment')
    #send_mail(subject='Feedback of my site', message=str(new_comment),
              #from_email=None,
              #recipient_list=['daisuke.zr@icloud.com'])
    #return HttpResponseRedirect('/comment/')



