from rest_framework import viewsets
from .serializers import CharacterSerializer
from .models import CharacterModel


class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CharacterModel.objects.all()
    serializer_class = CharacterSerializer