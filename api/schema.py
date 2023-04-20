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


class CreatPost(graphene.relay.ClientIDMutation):
    post= graphene.Field(PostData)
    class Input:
        title= graphene.String()
        body= graphene.String()
        user= graphene.Int()
    def  mutate_and_get_payload(self,info,**kwargs):
        title= kwargs.get("title") 
        body= kwargs.get("body")
        user= kwargs.get("user")    
        post= Post.objects.create(title=title, body=body, user=user)
        return CreatPost(post)

class Mutation:
    create_post= CreatPost.Field()
