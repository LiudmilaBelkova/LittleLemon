from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        #fields = ['url', 'username', 'email', 'groups']
        fields = ['id', 'username', 'email', 'password', 'groups']
        # extra_kwargs = {
        #     'password': {"write_only": True}
        # }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)        