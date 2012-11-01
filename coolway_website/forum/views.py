# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
import django.db
from ..models.post import Post



def save_post(request):
    p = Post(company_id=1,authority='public',is_top='y',
        status='pub',category_id=1,user_id=2,user_name='zpxu',title='first',content='first content')
    p.save()
    post_list = Post.objects.all()
    size = len(post_list)
    return render_to_response('forum/save.html', {'size': size})

def post_list(request):
    post_list = Post.objects.all()
    return render_to_response('forum/list.html', {'post_list': post_list})


def run_single_value_query(query, *params):
    """
    Helper: run a query returning a single value (e.g. a COUNT) and return the value.
    """
    c = django.db.connections['default'].cursor()
    c.execute(query, params)
    return c.fetchone()[0]