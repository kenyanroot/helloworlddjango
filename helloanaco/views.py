import base64
from datetime import datetime
from  django.http import HttpResponse
import keys
import requests
from django.shortcuts import render
from django.views import View
from requests.auth import HTTPBasicAuth


# Create your views here.


def acess_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL= "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    print(r.json())
    json_response=r.json()
    my_acess_token=json_response['access_token']
    print(my_acess_token)

    return my_acess_token



# 2020-08-25 19:35:51.573044


def homepage(request):
    return render(request, 'mpesa/stingo.html')


class Viewclass(View):

        def get(self, request):

            pass

        def post(self, request):
            phone_number = request.POST['phone']
            comment = request.POST['comment']
            name = request.POST['firstname']



            print(phone_number,comment,name)

            unformatted_time = datetime.now()

            formatted_time = unformatted_time.strftime('%Y%m%d%H%M%S')

            data_to_encode = keys.business_short_code + keys.lipa_na_mpesa_passkey + formatted_time

            encoded_string = base64.b64encode(data_to_encode.encode())

            decoded_password = encoded_string.decode('utf-8')

            print(formatted_time)

            my_acess_token = acess_token()
            print(acess_token)

            def lipa_na_mpesa():
                access_token = my_acess_token
                api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
                headers = {"Authorization": "Bearer %s" % access_token}
                request = {
                    "BusinessShortCode": keys.business_short_code,
                    "Password": decoded_password,
                    "Timestamp": formatted_time,
                    "TransactionType": "CustomerPayBillOnline",
                    "Amount": "1",
                    "PartyA": phone_number,
                    "PartyB": keys.business_short_code,
                    "PhoneNumber": phone_number,
                    "CallBackURL": "https://projectgreenfield.herokuapp.com/",
                    "AccountReference": "12345",
                    "TransactionDesc": "Testing mpesa app"
                }

                response = requests.post(api_url, json=request, headers=headers)

                print(response.text)

            lipa_na_mpesa()

            return HttpResponse("Please check your phone.If you have any balance left you should receieve an stk push.Otherwise an mpesa message will be good enough for you😊👍. Thank you for helping me test my system and have a nice day ahead🦧😎. With regards,Anaco🎩"
                                )

        def sender(self, comment,name,phone_number):
            print(comment,name,phone_number)



