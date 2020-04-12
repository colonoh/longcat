from rest_framework import serializers

from sluggen.models import Slug


class SlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slug
        fields = '__all__'

class SlugCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slug
        fields = ['url']
