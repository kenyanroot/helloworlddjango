import requests

from helloanaco.helloanaco.tokengenerator import acess_token

my_acess_token=acess_token()




def reg_url():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_acess_token}
    request = {"ShortCode": " ",
               "ResponseType": " Completed",
               "ConfirmationURL": "https://projectgreenfield.herokuapp.com/",
               "ValidationURL": "https://projectgreenfield.herokuapp.com/"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

#reg_url()


def stimulatectob():
    access_token = my_acess_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {"ShortCode": " ",
               "CommandID": "CustomerPayBillOnline",
               "Amount": "2",
               "Msisdn":"",
               "BillRefNumber": "12332"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

