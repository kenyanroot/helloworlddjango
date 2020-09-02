import requests

from mainapp.tokengenerator import acess_token

my_acess_token=acess_token()




def reg_url():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_acess_token}
    request = {"ShortCode": "601407",
               "ResponseType": " Completed",
               "ConfirmationURL": "https://firefly-m.herokuapp.com",
               "ValidationURL": "https://firefly-m.herokuapp.com/api/payments/lnms"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

reg_url()




