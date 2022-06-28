sum=0
while(True):
    userinput=int(input("enter the price of item: \n"))
    if(userinput !='q'):
        print("thank you for using ME")
        sum=sum+userinput
        print("you bill isL ",sum)
    else:
        print("thank you!")