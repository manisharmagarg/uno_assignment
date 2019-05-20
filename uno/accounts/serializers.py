# restframework imports
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework import exceptions

# djnago imports
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
#utils
from utils import res_codes

# in house apps import
from .models import User

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    first_name = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    last_name = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(
        min_length=8,
        style={
            'input_type': 'password', 
        }
    )

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True, },
        }

    def create(self, validated_data):
        user_obj = User.objects.create(**validated_data)
        user_obj.set_password(validated_data['password'])
        user_obj.save()
        return user_obj

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(
        style={
            'input_type': 'password', 
        }
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivate"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide email and password both"
            raise exceptions.ValidationError(msg)
        return data


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True, 
        style={
            'input_type': 'password', 
        }
    )
    new_password = serializers.CharField(
        required=True,
        style={
            'input_type': 'password', 
        }
    )

    class Meta:
        fields = [
            'password',
            'new_password',
        ]
        extra_kwargs = {
            'password': {'write_only': True, },
        }

    def validate_password(self, data):
        if not check_password(data, self.instance.password):
            raise serializers.ValidationError(
                    res_codes.get_response_dict(
                        res_codes.WRONG_PASSWORD_ENTERED
                    )
                )
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
