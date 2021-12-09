from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True,
        required=True,
        style={"input_type":"password"})
    password2 = serializers.CharField(write_only=True,
        required=True,label='Password Again',
        style={"input_type":"password"})
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'password','password2']
        extra_kwargs = {
            'password2' : {'write_only':True}
        }
    def create(self,data):
        password = data.pop('password2')
        user =  User.objects.create(**data)
        user.password = make_password(password)
        user.save()
        return user
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return data 