# from django.shortcuts import render

from rest_framework import generics

from sluggen.models import Slug
from sluggen.serializers import SlugListSerializer, SlugCreateSerializer


# POST
# create a new slug from a URL
class SlugCreate(generics.CreateAPIView):
    '''
    Create a new slug
    '''
    serializer_class = SlugCreateSerializer

    # def create(self, request):
    #     print('setting slug')
    #     self.slug = 'abc'
    
    # def perform_create(self, serializer):
    #     print('Performing create!!!')
    #     serializer.save()

class SlugList(generics.ListAPIView):
    '''
    List all of the slugs
    '''
    queryset = Slug.objects.all()
    serializer_class = SlugListSerializer

# GET
# read a URL for a pecific slug
