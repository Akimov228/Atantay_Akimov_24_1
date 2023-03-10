from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserValidateSerializer, UserLoginSerializer
from django.contrib.auth import authenticate



@api_view(['POST'])
def registration_view(request):
    serializer = UserValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(username=serializer.validated_data.get('username'),
                             password=serializer.validated_data.get('password'))
    # User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authorization_view(request):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(username=serializer.validated_data.get('username'),
                        password=serializer.validated_data.get('password'))
    # user = authenticate(**serializer.validated_data)

    '''here we are giving to user token.key if authorization passed'''
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(data=status.HTTP_401_UNAUTHORIZED)
