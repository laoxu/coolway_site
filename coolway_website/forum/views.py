# -*- encoding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.views.generic.list_detail import object_list

from ..utils.dbutils import *
from ..models.post import Post,COMPANY_AUTHORITY_POST, PUB_STATUS_POST,PUBLIC_AUTHORITY_POST
import logging

log = logging.getLogger(__name__)

##发帖
def post_create(request,post_id):
    p = Post(company_id=1,authority='public',is_top='y',
        status='pub',category_id=1,user_id=2,user_name='zpxu',title='first',content='first content')
    p.save()
    post_list = Post.objects.all()

    size = len(post_list)
    return render_to_response('forum/save.html', {'size': size})

#帖子列表:根据帖子id展示
def post_list(request):
    return object_list(request,
        queryset = Post.objects.filter(status=PUB_STATUS_POST, authority=PUBLIC_AUTHORITY_POST),
        paginate_by = 25,
        template_name ='forum/list.html',
        template_object_name='post'
        )

#帖子详情页
def post_detail(request,post_id):
    try:
        postId = int(postId)
    except ValueError:
        raise Http404
    post = get_object_or_404(Post, id=postId)
    return render_to_response('forum/detail.html',{'detail':post})

#回帖:回帖成功跳转到帖子最后一页
def post_reply(request,postId):
    pass

def function():
    pass