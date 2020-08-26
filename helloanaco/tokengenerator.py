from requests.auth import HTTPBasicAuth
import keys
import requests


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
