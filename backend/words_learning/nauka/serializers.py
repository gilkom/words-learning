from rest_framework import serializers
from django.contrib.auth import authenticate
from nauka.models import Word, Learning, User

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class LearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learning
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length = 4, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type':'password'},
        trim_whitespace=False,
        write_only=True
    )
    user_id = serializers.IntegerField(read_only=True) 

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:

            user = authenticate(request=self.context.get('request'),
                                username=username, password = password)
            if not user:
                msg="Access denied: wrong username or password."
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = "Both 'username' and 'password' are required."
            raise serializers.ValidationError(msg, code='authorization')
        
        attrs['user'] = user
        attrs['user_id'] = user.id
        return attrs