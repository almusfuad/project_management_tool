from rest_framework import serializers
from django.contrib.auth.models import User
from .utils import is_email_unique


class UserSerializer(serializers.ModelSerializer):
      email = serializers.EmailField()


      class Meta:
            model = User
            fields = [
                  "id",
                  "username",
                  "email",
                  "first_name",
                  "last_name",
            ]

      def validate_email(self, value):
            if not is_email_unique(value):
                  raise serializers.ValidationError("Email already exists")
            return value
      


