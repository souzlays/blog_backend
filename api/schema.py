import graphene
from django.conf import settings
from api.models import Post


class PostData(graphene.ObjectType):
    title= graphene.String()
    body= graphene.String()
    user= graphene.Int()
    date= graphene.DateTime()

class Query:
    version= graphene.String ()
    def resolve_version(self,info,**kwargs):
        return settings.VERSION

    posts= graphene.List(PostData)
    def resolve_posts(self,info,**kwargs):  
        return Post.objects.filter(**kwargs)                                

