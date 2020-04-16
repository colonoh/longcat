from rest_framework import serializers

from sluggen.models import Slug
from sluggen.utils import generate


class SlugListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slug
        fields = '__all__'

class SlugCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slug
        fields = ['url']

    def create(self, validated_data):
        url = validated_data['url']
        slug = generate(url, 3)
        obj = Slug.objects.create(url=url, slug=slug)
        return obj
