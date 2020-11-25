from rest_framework import serializers

from .models import TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id','username', 'first_name', 'last_name', 'role',
                    'description', 'start_work', 'end_work', 'wage']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['username', 'password']
        password = serializers.CharField(style={'input_type': 'password'}, 
                                            write_only=True)

    def create(self):
        user = TeamMember.objects.create(username=self.validated_data['username'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user
