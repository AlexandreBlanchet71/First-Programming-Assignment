from firebase import firebase
import random

firebase = firebase.FirebaseApplication('https://assignment1-1202b.firebaseio.com/groupe',None)

a=input("Would you want to start this program ? 0 is Yes, other number is No")

if a==0 :
    k=random.randrange(100000,999999,6)

else :
    print("You do not want to use this database so there will be an error")
    

result=firebase.post('/groupe',{'ID':k})

