# -*- encoding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect,render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..utils.dbutils import *
from ..models.post import *
from ..models.postReply import *
from .forms import *
import logging

log = logging.getLogger(__name__)
POST_PAGE_SIZE=25
REPLY_PAGE_SIZE=30

##发帖
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            return HttpResponseRedirect('/thanks/') # Redirect after POST
        else:
            form = PostCreateForm() # An unbound form
    return render(request, 'contact.html', {'form': form,})

#帖子列表
#@login_required
def post_list(request):
    company_id = 1
    page = request.GET.get('page')
    try:
        company_id = int(company_id)
    except ValueError:
        raise Http404
    post_list = Post.objects.getPostAuthCompany().filter(company=company_id)
    paginator = Paginator(post_list, POST_PAGE_SIZE) # Show 25 posts per page
    posts = fetch_paged_object_list(paginator,page)
    form = PostCreateForm()
    return render(request,'post/list.html', {"posts": posts,"form":form})

#帖子详情页
def post_detail(request,post_id):
    page = request.GET.get('page')
    try:
        post_id = int(post_id)
    except ValueError:
        raise Http404
    post = Post.objects.visible().filter(pk=post_id)
    if post :
        reply_list = PostReply.objects.getByPost(post_id)
        paginator = Paginator(reply_list, REPLY_PAGE_SIZE)
        replys = fetch_paged_object_list(paginator,page)
    else:
        replys = []
    form = ReplyForm()
    return render(request,'post/detail.html',{'postObj':post,'replys':replys,"form":form})

#回帖:回帖成功跳转到帖子最后一页
#@login_required
def post_reply(request,post_id):
    user = request.user
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            
            
    pass


def fetch_paged_object_list(paginator,page):
    if page is None:
        page = 1
    try:
        value_list = paginator.page(page)
    except PageNotAnInteger:
        value_list = paginator.page(1)
    except EmptyPage:
        value_list = paginator.page(paginator.num_pages)
    return value_list

