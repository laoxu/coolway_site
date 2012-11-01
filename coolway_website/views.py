# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

from django.contrib.comments.models import Comment
from django.contrib.sitemaps import views as sitemap_views
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template
import datetime

# 首页
def index(request):
    current_date = datetime.datetime.now()
    return render_to_response('index.html', {'current_date': current_date})

# @cache_page(60*60*6)
# def sitemap(request):
#     return sitemap_views.sitemap(request, sitemaps={
#         'weblog': WeblogSitemap,
#         'flatpages': FlatPageSitemap,
#     })

def comments(request):
    return list_detail.object_list(
        request,
        queryset = Comment.objects.filter(is_public=True).order_by('-submit_date'),
        paginate_by = 30,
    )

@csrf_exempt
def donate_thanks(request):
    return direct_to_template(request, 'donate_thanks.html')


@requires_csrf_token
def server_error(request, template_name='500.html'):
    """
    Custom 500 error handler for static stuff.
    """
    return render(request, template_name)



