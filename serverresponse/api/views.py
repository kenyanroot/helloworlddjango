from django.contrib.auth.models import User
#from serverresponse.api.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from serverresponse.api.serializers import Mpesaserial
#from serverresponse.models import Lipanampesa

class LNMonlineapiview(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Mpesaserial
    permission_classes = [AllowAny]
    def create(self,request):
        print(request.data, "this is request.data")