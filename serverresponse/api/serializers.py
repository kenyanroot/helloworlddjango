from rest_framework import serializers
from serverresponse.models import LMNOnline


class  LNNOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LMNOnline
        fields = ['id']