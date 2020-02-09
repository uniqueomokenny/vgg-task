from rest_framework.serializers import ModelSerializer

from actions.models import Actions


class ActionsSerializer(ModelSerializer):

    class Meta:
        model = Actions
        fields = '__all__'
