import base64
from datetime import datetime
from  django.http import HttpResponse
import keys
from keys import business_short_code
import requests
from django.shortcuts import render
from django.views import View
from requests.auth import HTTPBasicAuth
import re

from django.contrib import messages



# Create your views here.
from greetings.models import Namecomment


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
    return render(request, 'mpesa/index.html')

def mpesaform(request):
    return render(request,'mpesa/form.html')

def tecnologies(request):
    return render(request ,'mpesa/tecnologies.html')
def about(request):
    return render(request, 'mpesa/about.html')



class Viewclass(View):

        def get(self, request):

            pass


        def post(self, request):

            phone_number = request.POST['phone']
            comment = request.POST['comment']
            name = request.POST['firstname']


            # INPUT VALIDATION
            print(phone_number, comment, name)

            if len(phone_number)!=12:
                messages.error(request,"Phone Number too short or too long!")
                return render(request,"mpesa/form.html")

            else:

                result = re.match('^[254]+$', phone_number[0:3])
                print(result)

                if result == None:
                    messages.error(request, "Number did not start with 254")

                    return render(request,"mpesa/form.html")



                else:


                    if phone_number.isnumeric() == True:

                        print("got it!")

                        # Generating timestamp
                        unformatted_time = datetime.now()

                        formatted_time = unformatted_time.strftime('%Y%m%d%H%M%S')

                        data_to_encode = keys.business_short_code + keys.lipa_na_mpesa_passkey + formatted_time

                        encoded_string = base64.b64encode(data_to_encode.encode())

                        decoded_password = encoded_string.decode('utf-8')

                        print(formatted_time)


                        # acces token

                        my_acess_token = acess_token()
                        print(acess_token)

                        # Brought this function here from mpesa.py in order to be able to acces the local variable phone_number

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
                                "PartyB":business_short_code,
                                "PhoneNumber": phone_number,
                                "CallBackURL": "https://firefly-m.herokuapp.com/api/payments/lnm/",
                                "AccountReference": "Anaco",
                                "TransactionDesc": "Testing mpesa app"
                            }

                            response = requests.post(api_url, json=request, headers=headers)

                            print(response.text)

                        lipa_na_mpesa()

                        user = Namecomment(name=name, comment=comment, phone_number=phone_number, )
                        user.save()

                        messages.success(request, "Sucessful. Please check your phone")

                        return render(request,"mpesa/form.html")
                    else:

                        messages.error(request, "Phone Number is not numeric")

                        return render(request,"mpesa/form.html")





















