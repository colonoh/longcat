from rest_framework import generics

from sluggen.models import Slug
from sluggen.serializers import SlugListSerializer, SlugCreateSerializer


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
    serializer_class = SlugListSerializer
