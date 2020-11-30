from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import TeamMemberSerializer
from .models import TeamMember


class UserViewSet(viewsets.ModelViewSet):

    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

    def get_permissions(self):
        '''Give permissions for methods'''
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
