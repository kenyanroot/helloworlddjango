
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from serverresponse.models import LMNOnline
from .serializers import LNNOnlineSerializer


class LNMCallbackapiview(CreateAPIView):
    queryset =LMNOnline.objects.all()
    serializer_class = LNNOnlineSerializer
    permission_classes = [AllowAny]
    def create(self,request):
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



        from  datetime import datetime
        sting_transaction_date=str(transaction_date)

        transaction_datetime= datetime.strptime(sting_transaction_date, "%Y%m%d%H%M%S")
        print(transaction_datetime)
        our_model=LMNOnline(
            Merchant_requestID=merchant_request_ID,
            #Checkout_requestID =checkout_request_ID,
            Resultcode =result_code,
            Resultdesc=result_desc,
            A_mmount  =ammount,
            Mpesa_receiptnumber =mpesa_receipt_number,
            Transactiondate =transaction_datetime,
            Phonenumber  =phone_number,)
        our_model.save()
        return Response({'our result code':"yeey its working!"})
    

