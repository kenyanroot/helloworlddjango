import re
number='25470627j8559'



result=re.match('^[254]+$', number[0:3])
print(result)
if  result == None:
    print("number did not start with 254")
else:
    if number.isnumeric()==True:


        print("got it!")

    else:
        print("not numeric")


j=number[:3]
print(j)