with open('currency.txt') as f:
    lines=f.readlines()
currencyDict={ }
for line in lines:
    parsed=line.split("\t")
    currencyDict[parsed[0]]=parsed[1]
print(currencyDict)

amount=int(input("enter amount: "))
   
print("enter the name of the currency you want to convert from these amount of Available options:\n ")
[print(item) for item in currencyDict.keys()]
currency=(input("please enter one of these values"))
print(f"{amount} INR is equal to{amount * float(currencyDict[currency])} {currency}")
