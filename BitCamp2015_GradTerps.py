import json
import requests
import math
from math import radians, cos, sin, asin, sqrt
import pygmaps

'''THIS MODULE ALLOWS US TO DISPLAY ALL THE CAPITAL ONE ATMs'''

print('Welcome to a simple graphical display of all our ATMs in United States ') 
req4 = requests.get('http://api.reimaginebanking.com:80/atms?key=CUSTeaddb70b37e59531e905b107af5801fd') #Request URL to get all ATMs from API
atms = req4.json() #Extracting all ATMs in form of a JSON file
no_of_atms = 0 #counter to indicate total number of ATMs
list1,list2 = [[]for _  in range(2)] #Two Empty Lists
for i in range(len(atms)):                  #Parsing through all the ATMs in the file extracted
    list1.append(atms[i]['geocode']['lat']) #Appending latitude information of all ATMs into list1
    list2.append(atms[i]['geocode']['lng']) #Appending longitude information of all ATMs into list2
    no_of_atms+=1 #Incrementing counter for No. of ATMs by 1
print('Total number of ATMs are',no_of_atms) #Printing Total No. of ATMs
mymap = pygmaps.maps(list1[int(no_of_atms/2)], list2[int(no_of_atms/2)], 4) #Creating pygmaps constructor as mymap
print('Map is generated...Please check it on your system')
for i in range(no_of_atms):                 #Parsing through range of all the ATMs
    mymap.addpoint(list1[i], list2[i], "#0000FF") #Adding pointer to show locations of all the ATMs in United States of America
mymap.draw('./atms.html') #Draw object to generate HTML map file to be accessed from system


'''THIS MODULE WILL RESULT IN ADDRESS OF NEAREST ATM FOR USER SPECIFIED LATITUDE AND LONGITUDE'''
'''IN PRACTICAL SCENARIO,IMAGINE USER LATITUDE AND LONGITUDE TO BE EXTRACTED USING LOCATION SERVICES IN MOBILE PHONE/VEHICLE OF USER'''
user_latitude = float(input("Please enter your latitude")) #user-specified latitude
user_longitude = float(input('Please enter your longitude')) #user-specified longitude
distances = [] #empty list to gather all the distances between user specified details and each ATM location details
user_longitude = math.radians(user_longitude) #converting longitude from degrees into radians
user_latitude = math.radians(user_latitude) #converting latitude from degress into radians
for j in range(no_of_atms): #Parsing through all the ATMs
    list2[j] = math.radians(list2[j]) #Converting all the ATM longitudes from degrees to radians
    list1[j] = math.radians(list1[j]) #Converting all the ATM latitudes from degress to radians
    dlon = list2[j] - user_longitude #difference in longitude values(in radians)
    dlat = list1[j] - user_latitude #difference in latitude values(in radians)
    a = sin(dlat/2)**2 + cos(user_latitude) * cos(list1[j]) * sin(dlon/2)**2 #Haversine formula 
    c = 2 * asin(sqrt(a))
    km = 6367 * c    
    distances.append(km) #Appending all the distances between user details and ATMs(obtained in kilometers)
min_distance = min(distances) #Finding minimum of all the distances obtained
print('The closest ATM is at',min_distance,'km') #Printing closest ATM accordingly
print("The address of the nearest ATM is",atms[distances.index(min_distance)]['address']) #Printing Address of nearest ATM analyzed through minimum distance
    

'''THIS MODULE ALLOWS US TO TRANSFER MONEY BETWEEN ACCOUNTS AUTHORIZED'''
print('Welcome to Capital One Banking Account transfers') #Welcome Message
req1=requests.get('http://api.reimaginebanking.com:80/customers/5516c07aa520e0066c9ac323/accounts?key=ENTeaddb70b37e59531e905b107af5801fd')#Request URL for customer1
cust1=req1.json() #Extracting Customer1 account details in JSON format
cust11=dict(cust1[0]) #Changing the extracted details into dictionary format
req2=requests.get('http://api.reimaginebanking.com:80/customers/5516c07aa520e0066c9ac324/accounts?key=ENTeaddb70b37e59531e905b107af5801fd')#Request URL for customer2
cust2=req2.json() #Extracting Customer2 account details in JSON format
cust21=dict(cust2[0]) #Changimg the extracted details into dictionary format
req3=requests.get('http://api.reimaginebanking.com:80/customers/5516c07aa520e0066c9ac325/accounts?key=ENTeaddb70b37e59531e905b107af5801fd')#Request URL for customer3
cust3=req3.json() #Extracting Customer3 account details in JSON format
cust31=dict(cust3[0]) #Changing the extracted details into dictionary format

def id12(): #Transfer function between customer1 and customer2
    bal1=cust11['balance'] #Extracting balance details of customer1
    bal2=cust21['balance'] #Extracting balance details of customer2
    print('Current balance of customer 1 is\n',bal1) #Printing current balance of Customer1
    print('Current balance of customer 2 is\n',bal2) #Printing current balance of Customer2
    print('1.Do you need deduction from customer1 and transfer to customer2?')
    print('2.Do you need deduction from customer2 and transfer to customer1?')
    a=input('Please chooose action needed to be performed(1 or 2)\n') #User Choice of transfer
    if(a == '1'): #If transfer is from customer1 to customer2
        deduction1=input('How much to deduct from customer1 and transfer to customer2?\n')#If transfer is from customer1 to customer2
        bal1=int(bal1) - int(deduction1) #Subtracting that deduction value from customer1 balance
        bal2=int(bal2) + int(deduction1) #Adding deduced value from customer1 to customer2
        print('New balance of customer1 is\n',bal1) #Printing new balance of customer1
        cust11['balance']=bal1 #Updating balance value in customer1 account details
        print('New balance of customer2 is\n',bal2) #Printing new balance of customer2
        cust21['balance']=bal2 #Updating balance value in customer2 account details
    elif(a == '2') : #If transfer is from customer2 to customer1
        deduction2=input('How much to deduct from customer2 and transfer to customer1?\n') #Taking Amount to be deducted as input
        bal2=int(bal2) - int(deduction2) #Subtracting that deduction value from customer2 balance
        bal1=int(bal1) + int(deduction2) #Adding deduced value from customer2 to customer1
        print('New balance of customer1 is\n',bal1)#Printing new balance of customer1
        cust11['balance']=bal1 #Updating balance value in customer1 account details
        print('New balance of customer2 is\n',bal2)#Printing new balance of customer2
        cust21['balance']=bal2 #Updating balance value in customer2 account details
    else: #If any other option is selected
        print('Sorry!!! Wrong Selection...Transaction cancelled') #Transaction Error

def id13(): #Transfer function between customer1 and customer3
    bal1=cust11['balance'] #Extracting balance details of customer1
    bal3=cust31['balance'] #Extracting balance details of customer3
    print('Current balance of customer 1 is\n',bal1) #Printing current balance of Customer1
    print('Current balance of customer 3 is\n',bal3) #Printing current balance of Customer2
    print('1.Do you need deduction from customer1 and transfer to customer3?') 
    print('2.Do you need deduction from customer3 and transfer to customer1?')
    a=input('Please chooose action needed to be performed(1 or 2)\n') #User Choice of transfer
    if(a == '1'): #If transfer is from customer1 to customer3
        deduction1=input('How much to deduct from customer1 and transfer to customer3?\n') #If transfer is from customer1 to customer3
        bal1=int(bal1) - int(deduction1) #Subtracting that deduction value from customer1 balance
        bal3=int(bal3) + int(deduction1) #Adding deduced value from customer1 to customer3
        print('New balance of customer1 is\n',bal1) #Printing new balance of customer1
        cust11['balance']=bal1 #Updating balance value in customer1 account details
        print('New balance of customer3 is\n',bal3)  #Printing new balance of customer3
        cust31['balance']=bal3 #Updating balance value in customer3 account details
    elif(a == '2'): #If transfer is from customer1 to customer3
        deduction2=input('How much to deduct from customer3 and transfer to customer1?\n')
        bal3=int(bal3) - int(deduction2) #Subtracting that deduction value from customer1 balance
        bal1=int(bal1) + int(deduction2) #Adding deduced value from customer1 to customer3
        print('New balance of customer1 is\n',bal1) #Printing new balance of customer1
        cust11['balance']=bal1 #Updating balance value in customer1 account details
        print('New balance of customer3 is\n',bal3) #Printing new balance of customer3
        cust31['balance']=bal3 #Updating balance value in customer3 account details
    else: #If any other option is selected
        print('Sorry!!! Wrong Selection...Transaction cancelled') #Transaction Error

def id32(): #Transfer function between customer2 and customer3
    bal3=cust31['balance'] #Extracting balance details of customer3
    bal2=cust21['balance'] #Extracting balance details of customer2
    print('Current balance of customer 3 is\n',bal3) #Printing current balance of Customer3
    print('Current balance of customer 2 is\n',bal2) #Printing current balance of Customer2
    print('1.Do you need deduction from customer3 and transfer to customer2?') 
    print('2.Do you need deduction from customer2 and transfer to customer3?')
    a=input('Please chooose action needed to be performed(1 or 2)\n') #User Choice of transfer
    if(a == '1'): #If transfer is from customer3 to customer2
        deduction1=input('How much to deduct from customer3 and transfer to customer2?\n')#If transfer is from customer3 to customer2
        bal3=int(bal3) - int(deduction1) #Subtracting that deduction value from customer3 balance
        bal2=int(bal2) + int(deduction1) #Adding deduced value from customer3 to customer2
        print('New balance of customer3 is\n',bal3) #Printing new balance of customer3
        cust31['balance']=bal3 #Updating balance value in customer3 account details
        print('New balance of customer2 is\n',bal2) #Printing new balance of customer2
        cust21['balance']=bal2 #Updating balance value in customer2 account details
    elif(a == '2'): #If transfer is from customer2 to customer3
        deduction2=input('How much to deduct from customer2 and transfer to customer3?\n') #If transfer is from customer2 to customer3
        bal2=int(bal2) - int(deduction2) #Subtracting that deduction value from customer2 balance
        bal3=int(bal3) + int(deduction2) #Adding deduced value from customer2 to customer3
        print('New balance of customer3 is\n',bal3) #Printing new balance of customer3
        cust31['balance']=bal3 #Updating balance value in customer3 account details
        print('New balance of customer2 is\n',bal2) #Printing new balance of customer2
        cust21['balance']=bal2 #Updating balance value in customer2 account details
    else:  #If any other option is selected
        print('Sorry!!! Wrong Selection...Transaction cancelled') #Transaction Error

print('1.Between acoounts specified by id1 & id2') #Choice1
print('2.Between accounts specified by id2 & id3') #Choice2
print('3.Between accounts specified by id3 & id1') #Choice3
choice=input('Please pick the accounts between which you need transfers\n') #Reading user choice of transfer        
if choice == '1': 
    id12() #Transfer between customer1 and customer2
elif choice == '2':
    id13() #Transfer between customer1 and customer3
elif choice == '3':
    id32() #Transfer between customer3 and customer2
else:
    print('Sorry!!! Wrong Selection...Transaction cancelled') #Transaction Error
    



