# from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from sluggen.models import Slug
from sluggen.serializers import SlugSerializer


@csrf_exempt
def slug_list(request):
    """
    List all code slugs, or create a new slug.
    """
    if request.method == 'GET':
        slugs = Slug.objects.all()
        serializer = SlugSerializer(slugs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SlugSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def slug_details(request, pk):
    """
    Retrieve, update or delete a code slug.
    """
    try:
        slug = Slug.objects.get(pk=pk)
    except Slug.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SlugSerializer(slug)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SlugSerializer(slug, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        slug.delete()
        return HttpResponse(status=204)