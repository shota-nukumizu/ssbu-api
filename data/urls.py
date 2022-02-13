from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('fighters', views.CharacterViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))
]