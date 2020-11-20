from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# from account.models import Account 
from django.contrib.auth.models import User

from .models import * 
from .serializers import * 


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.create()
            data['response'] = 'successfully registered new user.'
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def all_members_view(request):
    
    data = {}

    try:
        team_member = TeamMember.objects.values_list('inner_username', flat=True)
    except TeamMember.DoesNotExist:
        data['failed'] = 'There is no data'
        return Response(data=data)
    
    if request.method == 'GET':
        data['list of users'] = team_member
        return Response(data=data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def detail_team_member_view(request, slug):
    
    try:
        team_member = TeamMember.objects.get(inner_username=slug)
    except TeamMember.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TeamMemberSerializer(team_member)
        return Response(serializer.data)


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def create_team_member_view(request):

    if request.method == 'POST':
        serializer = TeamMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT', ])
@permission_classes([IsAuthenticated])
def update_team_member_view(request, slug):
    
    try:
        team_member = TeamMember.objects.get(inner_username=slug)
    except TeamMember.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = TeamMemberSerializer(team_member, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE', ])
@permission_classes([IsAuthenticated])
def delete_team_member_view(request, slug):
    
    try:
        team_member = TeamMember.objects.get(inner_username=slug)
    except TeamMember.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        operation = team_member.delete()
        data = {}
        if operation:
            data['success'] = 'delete successful'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)
        



