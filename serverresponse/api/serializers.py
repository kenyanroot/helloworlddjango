from rest_framework import serializers
from serverresponse.models import Lipanampesa


class  Mpesaserial(serializers.ModelSerializer):
    class Meta:
        model = Lipanampesa
        fields = ['id']