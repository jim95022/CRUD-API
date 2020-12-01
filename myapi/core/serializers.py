import re
from rest_framework import serializers

from .models import TeamMember


def password_validation(passwd):
    if not re.match(r"^(?=.*[A-Z])(?=.*\d).{8,}$", passwd):
            raise serializers.ValidationError({
                        'Error':'Password must contain at least eight characters, at least one number and uppercase letter.'
                        })
    return passwd


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        extra_kwargs = {'password': {'write_only': True, 'validators':[password_validation]}}
        fields = ['id', 'username','password', 'first_name', 'last_name', 'role',
                    'description', 'start_work', 'end_work', 'wage']

    def create(self, validated_data):
        user = TeamMember.objects.create_user(**validated_data)
        return user
