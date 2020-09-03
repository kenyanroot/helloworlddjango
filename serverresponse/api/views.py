from django.contrib.auth.models import User
#from serverresponse.api.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from serverresponse.api.serializers import LNNOnlineSerializer
from serverresponse.models import LMNOnline
from serverresponse.api.serializers import Mpesaserial
#from serverresponse.models import Lipanampesa

class LNMCallbackapiview(CreateAPIView):
    queryset = LMNOnline.objects.all()
    serializer_class = LNNOnlineSerializer
    permission_classes = [AllowAny]
    def create(self,request):
        print(request.data, "this is request.data")