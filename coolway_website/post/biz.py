
from ..models.post import Post,COMPANY_AUTHORITY_POST, PUB_STATUS_POST,PUBLIC_AUTHORITY_POST
from ..models.postReply import PostReply
from ..utils.dbutils import *

PAGE_ZIZE = 20

def createPost(userId,companyId,categoryId,title,content,authority):
    p = Post(company_id=companyId,authority=authority,is_top='y',
        status=PUB_STATUS_POST,category_id=categoryId,user_id=user_id,
        title=title,content=content)
    return p.save()

def getPosts(companyId,categoryId,page):

    pass

##
def getPostById(postId):
    return Post.objects.get(id=postId)


def getPostByCategory(categoryId,page):
    return Post.objects.filter(category=categoryId)[(page*PAGE_ZIZE)-1:(page*PAGE_ZIZE-1)+PAGE_ZIZE]

def getReplyByPostId(postId,page):
    return PostReply.objects.filter(post=postId)[5:10]

def savePost(title,content):
    pass


def replyPost(postId,content):
    pass












