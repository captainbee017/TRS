from django.http import Http404
from django.shortcuts import render, get_object_or_404

from rest_framework import mixins, generics, permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from trainer.serializers import TrainerIntroductionSerializer
from trainer.models import TrainerIntroduction


class MyUserPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

# Create your views here.

class TrainerIntroductionList(generics.ListCreateAPIView):
    queryset = TrainerIntroduction.objects.all()
    serializer_class = TrainerIntroductionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class TrainerIntroductionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainerIntroduction.objects.all()
    serializer_class = TrainerIntroductionSerializer
    permission_classes = (MyUserPermissions, )
