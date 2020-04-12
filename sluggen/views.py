# from django.shortcuts import render

from rest_framework import generics

from sluggen.models import Slug
from sluggen.serializers import SlugSerializer, SlugCreateSerializer


# POST
# create a new slug from a URL
class SlugCreate(generics.CreateAPIView):
    '''
    Create a new slug
    '''
    serializer_class = SlugCreateSerializer

class SlugList(generics.ListAPIView):
    '''
    List all of the slugs
    '''
    queryset = Slug.objects.all()
    serializer_class = SlugSerializer

# GET
# read a URL for a pecific slug
