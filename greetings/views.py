from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def processing(request):


    if request.method=='POST':
        global phone_number
        firstname=request.POST['firstname']
        phone_number = 'it worked'#request.POST['phone']

        comments= request.POST['comment']


    else:
        return render(request,'mpesa/mpesa.html')
