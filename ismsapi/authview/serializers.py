from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
import bcrypt

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """

    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        #print("data >>>", data.get('password'))
        email = data.get('email')
        password = data.get('password')
        tempuserObj = User.objects.get(email=email)
        print("data >>>",len(tempuserObj.password))

        user = bcrypt.checkpw(password.encode('utf-8'), tempuserObj.password.encode('utf-8')) #check_password(password ,tempuserObj.password)
        print("user >>>", user)
        #user =    authenticate(**data)
        if user:
            return tempuserObj
        raise serializers.ValidationError("Incorrect Credentials")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'