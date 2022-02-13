from rest_framework import serializers
from .models import CharacterModel


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterModel
        fields = '__all__'