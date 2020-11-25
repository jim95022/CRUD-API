from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import TeamMemberSerializer, RegistrationSerializer
from .models import TeamMember


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        '''Display all users'''
        queryset = TeamMember.objects.all()
        serializer = TeamMemberSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        '''Create a new user. Method does not require authorization'''
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        '''Display information by user's ID'''
        queryset = TeamMember.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TeamMemberSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        '''Update some features of the user'''
        queryset = TeamMember.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TeamMemberSerializer(user, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update successful'
            return Response(data=data)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        '''Delete the user'''
        queryset = TeamMember.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        operation = user.delete()
        data = {}
        if operation:
            data['success'] = 'delete successful'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)

    def get_permissions(self):
        '''Give permissions for methods'''
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

