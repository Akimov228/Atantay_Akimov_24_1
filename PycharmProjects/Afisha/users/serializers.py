from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class ConfirmationSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(max_length=6)
    def validate_confirmation_code(self, value):
        user = self.context.get('user')
        if not user.profile.confirmation_code == value:
            raise serializers.ValidationError('Invalid confirmation code')
        user.profile.is_active = True
        user.profile.save()
        return value


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserValidateSerializer(UserLoginSerializer):


    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')



