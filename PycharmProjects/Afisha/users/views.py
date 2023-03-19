from random import choice
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from .models import *
from .serializers import UserValidateSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
# from rest_framework.generics import *




class RegistrationUserAPIView(APIView):

    def post(self, request):
        serializer = UserValidateSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(username=serializer.validated_data.get('username'),
                                            password=serializer.validated_data.get('password'))
            code = choice(range(100000, 999999))
            confirmation = Profile.objects.create(user=user, code=code)
            return Response({'status': 'User registered', 'code': confirmation.code}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserAuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data.get('username'),
                            password=serializer.validated_data.get('password'))
        # user = authenticate(**serializer.validated_data)

        '''here we are giving user token.key if authorization passed'''
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(data=status.HTTP_401_UNAUTHORIZED)


class UserConfirmationAPIView(APIView):
    def post(self, request):
        code = request.data.get('code')
        confirmation = get_object_or_404(Profile, code=code)
        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete()
        return Response({'status': 'User activated'}, status=status.HTTP_200_OK)



# @api_view(['POST'])
# def registration_view(request):
#     serializer = UserValidateSerializer(data=request.data)
#     if serializer.is_valid():
#         user = User.objects.create_user(username=serializer.validated_data.get('username'),
#                                         password=serializer.validated_data.get('password'))
#         code = choice(range(100000, 999999))
#         confirmation = Profile.objects.create(user=user, code=code)
#         return Response({'status': 'User registered', 'code': confirmation.code}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def authorization_view(request):
#     serializer = UserLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = authenticate(username=serializer.validated_data.get('username'),
#                         password=serializer.validated_data.get('password'))
#     # user = authenticate(**serializer.validated_data)
#
#     '''here we are giving user token.key if authorization passed'''
#     if user:
#         token, created = Token.objects.get_or_create(user=user)
#         return Response(data={'key': token.key})
#     return Response(data=status.HTTP_401_UNAUTHORIZED)
