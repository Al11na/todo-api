from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class RegistrationSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'email': {'required': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Расширяет стандартный сериализатор SimpleJWT,
    чтобы при логине отдавать вместе с токенами и данные пользователя.
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            'id':       self.user.id,
            'username': self.user.username,
            'email':    self.user.email,
        }
        return data
