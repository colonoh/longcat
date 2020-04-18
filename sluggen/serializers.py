from rest_framework import serializers

from sluggen.models import Slug
from sluggen.utils import generate_new_slug


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
        slug = generate_new_slug(3)
        return Slug.objects.create(url=url, slug=slug)
