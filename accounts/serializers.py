from rest_framework import serializers
from . models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # accept password from request, do not sent is back in response
                                            # can be written , but cannot read(password)

    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'],is_admin=False)
        return user # new registeration is held here