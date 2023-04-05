loans= ["Emergency Loan","Special Loan For Bank Customers",
       "Loan For Retirements"]

for loan in loans:
    print (loan) 

a=1 #print the second term of loans list
for a in range(len(loans)):
         print (loans[a])

b=4 #print the output of the term from outside of loans list
if b in range(len(loans)):
    print (loans[b])
else:
    print ("b value isnt in range of loans list ")      


for i in range(4,8): #print the integers from 4 to 8
    print (i)

for i in range(2,14,4): #print the integers from 2 to 14 increase by 4
    print (i)