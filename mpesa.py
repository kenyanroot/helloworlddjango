import requests
import keys
from datetime import datetime
import base64
from requests.auth import HTTPBasicAuth


unformatted_time=datetime.now()

formatted_time= unformatted_time.strftime('%Y%M%H%m%S')

data_to_encode=keys.business_short_code + keys.lipa_na_mpesa_passkey + formatted_time

encoded_string= base64.b64encode(data_to_encode.encode())

decoded_password=encoded_string.decode('utf-8')





consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print(r.json())
json_response=r.json()
my_acess_token=json_response['access_token']
print(my_acess_token)


def lipa_na_mpesa():
    access_token = json_response#"SGFZjIAiHbqlBtdzgeFGy96IuIRA"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": keys.business_short_code,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": " 1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_short_code,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://ip_address:port/callback",
        "AccountReference": "12345",
        "TransactionDesc": "Testing mpesa app"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

