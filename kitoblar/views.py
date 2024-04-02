from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import *
from .forms import CommentView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
def Categoriya(request,id):
    categoriya=Tillar.objects.all()
    tillar=get_object_or_404(Tillar,pk=id)
    kitoblar=tillar.tillar.all()
    data={
        'kitoblar':kitoblar,
        'categoriya':categoriya
    }
    return render(request,'kitoblar/categoriya.html',context=data)


def Detail(request,id):
    kitob=get_object_or_404(Kitob,pk=id)
    form=CommentView()
    data={
        "kitob":kitob,
        'form':form
    }

    return render(request,'kitoblar/detail_.html',context=data)


class AddComment(LoginRequiredMixin,View):
    def post(self,request,id):
        kitob=Kitob.objects.get(id=id)
        form=CommentView(request.POST)

        if form.is_valid():
             Comment.objects.create(
                user=request.user,
                kitob=kitob,
                comment_text=form.cleaned_data['comment_text'],
                stars_given=form.cleaned_data['stars_given'])
        return redirect(reverse('kitoblar:detail_page',kwargs={'id':kitob.id }))
 

            

