from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics

from sluggen.models import Slug
from sluggen.serializers import SlugListSerializer, SlugCreateSerializer


class SlugCreate(generics.CreateAPIView):
    '''
    Create a new slug
    '''
    serializer_class = SlugCreateSerializer

    # TODO: this needs to return the slug!!!

class SlugList(generics.ListAPIView):
    '''
    List all of the slugs
    '''
    queryset = Slug.objects.all()
    serializer_class = SlugListSerializer

def redirect_view(request, slug):
    '''
    If this slug exists, redirect to its URL.
    '''
    object = get_object_or_404(Slug, slug=slug)
    return redirect(object.url)
