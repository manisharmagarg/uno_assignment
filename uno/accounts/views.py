from django.shortcuts import render

# restframework imports
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

#djnago imports
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login as django_login, logout as django_logout
from django.utils import timezone

from .serializers import (
	UserCreateSerializer, 
	UserLoginSerializer,
	ChangePasswordSerializer,
)

from utils import res_codes
from django.core.mail import send_mail
from .models import AccountSettings

User = get_user_model()


class SignUpView(APIView):
	serializer_class = UserCreateSerializer

	def post(self, request, *args, **kwargs):
		data = request.data.copy()
		serializer = self.serializer_class(data=data)
		if serializer.is_valid():
			user_obj = serializer.save(is_active=False)
			host_name = 'http://127.0.0.1:8000'
			subject = 'verify email'
			conformations_email = '{}/api/accounts/email-conformation/{}/'.\
						format(
							host_name, 
							user_obj.User.activation_key
						)
			send_mail(
			    subject,
			    conformations_email,
			    'anaconda.wb@gmail.com',
			    [user_obj.email],
			)

			return Response(
				res_codes.get_response_dict(
					res_codes.SIGNUP_SUCCESS,
					serializer.data,
				),
				status=status.HTTP_201_CREATED,
			)
		return Response(
			res_codes.get_response_dict(
				res_codes.INVALID_POST_DATA,
				serializer.errors,
			),
			status=status.HTTP_400_BAD_REQUEST
		)


class EmailConformationView(APIView):
	def get(self, request, *args, **kwargs):
		activation_key = kwargs.get('activation_key')
		account_setting_obj = AccountSettings.objects.get(
			activation_key=activation_key
		)
		key_expire = account_setting_obj.key_expire
		if key_expire > timezone.now():
			print('i ma here', key_expire)
			account_setting_obj.user.is_active = True
			account_setting_obj.user.save()
			return Response({
					'status': 'User register successfully',
					'login_url': '/api/accounts/login/'
				})
		else:
			account_setting_obj.user.delete()
			return Response({
					'status': 'User Not register',
					'messages' : "key_expire'"
				})


class LoginView(APIView):
	serializer_class = UserLoginSerializer

	def post(self, request, *args, **kwargs):
		data = request.data.copy()
		serializer = self.serializer_class(data=data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data["user"]
		django_login(request, user)
		token, create = Token.objects.get_or_create(user=user)
		return Response(
			{
				"token": token.key,
				"User": user.get_full_name()
			},
			status=200
		)


class LogOutView(APIView):
	authentication_classes = (TokenAuthentication, )

	def get(self, request, format=None):
		django_logout(request)
		return Response(
			status=204
		)


class PasswordResetApiView(APIView):
	permissions = (IsAuthenticated,)
	serializer_class = ChangePasswordSerializer

	def put(self, request, *args, **kwargs):
		data = request.data.copy()
		serializer = self.serializer_class(
			request.user,
			data=data
			)
		if serializer.is_valid():
			serializer.save()
			return Response(
				res_codes.get_response_dict(
					res_codes.PASSWORD_UPDATE_SUCCESS,
				),
				status=status.HTTP_200_OK,
			)
		return Response(
			res_codes.get_response_dict(
				res_codes.INVALID_POST_DATA,
				serializer.errors
			),
			status=status.HTTP_400_BAD_REQUEST
		)
