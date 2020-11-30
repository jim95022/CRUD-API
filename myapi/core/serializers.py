import re
from rest_framework import serializers

from .models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'role',
                    'description', 'start_work', 'end_work', 'wage']


    def create(self, validated_data):
        if not re.match(r"^(?=.*[A-Z])(?=.*\d).{8,}$", validated_data['password']):
            raise serializers.ValidationError({
                        'Error':'Password must contain at least eight characters, at least one number and uppercase letter.'
                        })
        user = TeamMember.objects.create_user(**validated_data)
        return user
