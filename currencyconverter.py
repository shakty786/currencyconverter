# Currency Converter
print("____________________________")
print ("Hey!I am  CurrencyConvrter")
with open('currency.txt') as f:
    lines= f.readlines()
  
Invcurrency={}    
for line in lines:
    parse=line.split("\t")
    Invcurrency[parse[0]]=parse[2] 
 
for key in Invcurrency.keys():
    print(key)
    print ("\n") 
amount=float(input("Enter the amount"))#Taking Inputonverter     
source= input ("Please select the source currency from the above list\n")  
print("you choose",source) 
print ("\n")

for key in Invcurrency.keys():
    if source in key:
        INR=float(Invcurrency[key])*amount  
       # print (f"{amount} {source} is equal to {INR} Indian Rupee")   
        break
        
currencyDict={}# creating an empty Dictionary
for line in lines:
    parsed=line.split("\t") 
    currencyDict[parsed[0]]=parsed[1]
    

#for key in currencyDict.keys():
    #value=currencyDict[key]
    #print (key)
    #print ("\n")     
    
key1=input("Please select one of these in which you want to convert your money")
print("\n")
for key in currencyDict.keys():
    if key1 in key:
        value=float(currencyDict[key])*INR
        print(f" {amount} {source} is equal to {value} {key1}") 
        break
      
print("\n")
print("Thanks for using !")
       
print("__________________")
