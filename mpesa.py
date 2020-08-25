import requests
import keys
from datetime import datetime
import base64
from tokengenerator import acess_token
#2020-08-25 19:35:51.573044

unformatted_time=datetime.now()

formatted_time= unformatted_time.strftime('%Y%m%d%H%M%S')

data_to_encode=keys.business_short_code + keys.lipa_na_mpesa_passkey + formatted_time

encoded_string= base64.b64encode(data_to_encode.encode())

decoded_password=encoded_string.decode('utf-8')


print(formatted_time)


my_acess_token=acess_token()
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
        "PartyA": keys.phone_number,
        "PartyB": keys.business_short_code,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://projectgreenfield.herokuapp.com/",
        "AccountReference": "12345",
        "TransactionDesc": "Testing mpesa app"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

lipa_na_mpesa()

