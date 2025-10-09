from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

# Custom user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['id', 'followers']


# Register serializer with token generation
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)  # Return token after registration

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'token']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )
        # Create a token and attach it to the user
        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        return user


# Login serializer with token retrieval
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if not user:
            raise serializers.ValidationError("Invalid credentials")

        token, created = Token.objects.get_or_create(user=user)
        return {
            'username': user.username,
            'token': token.key
        }