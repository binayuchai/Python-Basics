with open('currencyConverter/rate.txt') as f:
    data = f.readlines()
    
    
currencyDict = {}    

for line in data:
        parsed = line.split('\t')
        currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount:\n"))
print("""Enter the name of currency you want to convert this amount to:
Available Currency:
      """)
[print(item) for item in currencyDict.keys()] # one line code for printing the keys of dictionary
currency = input("Please choose one of these option\n")
calculate = amount * float(currencyDict[currency])
print(f"{amount} NPR is equal to {calculate} {currency}")
