# -*- encoding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..utils.dbutils import *
from ..models.post import *
from ..models.postReply import *
import logging

log = logging.getLogger(__name__)
POST_PAGE_SIZE=25
REPLY_PAGE_SIZE=30

##发帖
@login_required
def post_create(request):
    # p = Post(company_id=1,authority='public',is_top='y',
    #     status='pub',category_id=1,user_id=2,user_name='zpxu',title='first',content='first content')
    # p.save()
    # post_list = Post.objects.all()
    #request.

    size = len(post_list)
    return render_to_response('post/save.html', {'size': size})


#帖子列表
#@login_required
def post_list(request):

    company_id=1
    page = request.GET.get('page')
    try:
        company_id = int(company_id)
    except ValueError:
        raise Http404
    post_list = Post.objects.getPostAuthCompany().filter(company=company_id)
    paginator = Paginator(post_list, POST_PAGE_SIZE) # Show 25 posts per page
    posts = fetch_paged_object_list(paginator,page)
    return render_to_response('post/list.html', {"posts": posts})

#帖子详情页
def post_detail(request,post_id):
    page = request.GET.get('page')
    try:
        post_id = int(post_id)
    except ValueError:
        raise Http404
    post = Post.objects.filter(pk=post_id)
    if post :
        reply_list = PostReply.objects.getByPost(post_id)
        paginator = Paginator(reply_list, REPLY_PAGE_SIZE)
        replys = fetch_paged_object_list(paginator,page)
    else:
        replys = []
    return render_to_response('post/detail.html',{'post':post,'replys':replys})

#回帖:回帖成功跳转到帖子最后一页
#@login_required
def post_reply(request,post_id):
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

