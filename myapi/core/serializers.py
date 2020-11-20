from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'first_name', 'last_name', 'inner_username', 'role', 'is_active', 'description', 'start_work', 'end_work', 'wage']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def create(self):
        user = User.objects.create(username=self.validated_data['username'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user
