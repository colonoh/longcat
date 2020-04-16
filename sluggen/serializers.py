from rest_framework import serializers

from sluggen.models import Slug


class SlugListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slug
        fields = '__all__'

class SlugCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slug
        fields = ['url']
