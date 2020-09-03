from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import LNNOnlineSerializer
from serverresponse.models import LMNOnline


class LNMCallbackapiview(CreateAPIView):
    queryset = LMNOnline.objects.all()
    serializer_class = LNNOnlineSerializer
    permission_classes = [AllowAny]
    def create(self,request):
        print(request.data, "this is request.data")