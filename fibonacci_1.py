#lets play with fibonacci
n=int(input("enter the value  "))
no_1=0
no_2=1
while no_2<n:
    print(no_2,end= " ")
    no_1,no_2=no_2,no_1+no_2
