from rest_framework import serializers

from .models import CustomUser


class ConfirmationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    """
    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Нельзя использовать "me"')
        return value
    """


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'bio', 'email',
                  'role']
        lookup_field = 'username'


class CustomUserPATCHSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'bio', 'email', ]
        lookup_field = 'username'


class ConfirmationCodeSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()
