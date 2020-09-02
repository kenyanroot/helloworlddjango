import requests
import requests

from mainapp.tokengenerator import acess_token

my_acess_token=acess_token()




#def reg_url():
    #access_token = my_acess_token
    #api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    #headers = {"Authorization": "Bearer %s" % my_acess_token}
   # request = {"ShortCode": "601407",
              # "ResponseType": "Completed",
              # "ConfirmationURL": "https://firefly-m.herokuapp.com/api/payments/lnms",
               #"ValidationURL": "https://firefly-m.herokuapp.com/api/payments/lnms"}

    #response = requests.post(api_url, json=request, headers=headers)

    #print(response.text)


#reg_url()

def simulatec2b():
    access_token = my_acess_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {"ShortCode": "601407",
               "CommandID": "CustomerPayBillOnline",
               "Amount": "1",
               "Msisdn": "254706278553",
               "BillRefNumber": "1234"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

simulatec2b()







