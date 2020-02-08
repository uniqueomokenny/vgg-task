from django.contrib.auth import get_user_model

from rest_framework import serializers
from django.db import transaction


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=120, write_only=True)

    class Meta:
        model = User
        exclude = ("is_superuser", "is_staff", "is_active",
                   "groups", "user_permissions")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if 'confirm_password' not in data:
            raise serializers.ValidationError('confirm password is required')

        if ('password' in data) and ('confirm_password' in data) and (data['password'] != data['confirm_password']):
            raise serializers.ValidationError(
                'password and confirm password must match')

        return data

    def save(self, *args, **kwargs):
        self.validated_data.pop('confirm_password', None)
        return super().save(**kwargs)

    def create(self, validated_data):

        with transaction.atomic():
            user = super().create(validated_data)
            user.set_password(user.password)
            user.save(update_fields=["password"])

            return user
