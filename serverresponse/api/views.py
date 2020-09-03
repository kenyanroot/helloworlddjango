from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import LNNOnlineSerializer
from serverresponse.models import LMNOnline


class LNMCallbackapiview(CreateAPIView):
    queryset = LMNOnline.objects.all()
    serializer_class = LNNOnlineSerializer
    permission_classes = [AllowAny]
    def create(self,request,**kwargs):
        print(request.data, "this is request.data")
        merchant_request_ID=request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_ID=request.data['Body']['stkCallback']['CheckoutRequestID']
        result_code=       request.data ['Body']['stkCallback']['ResultCode']
        result_desc=       request.data['Body']['stkCallback']['ResultDesc']
        ammount=           request.data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        print(ammount)
        mpesa_receipt_number= request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        transaction_date=  request.data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value']

        phone_number=      request.data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

        print(phone_number)
        print(transaction_date)
        print(mpesa_receipt_number)
        print(result_code)
        print(result_desc)
        print(merchant_request_ID)
        print(checkout_request_ID)
