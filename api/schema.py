import graphene
from django.conf import settings

class Query:
    version= graphene.String ()
    def resolve_version(self,info,**kwargs):
        return settings.VERSION