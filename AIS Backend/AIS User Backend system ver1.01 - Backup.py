"""
Created on Thu Jun  4 13:46:36 2020

Author: Shahazureen Ikwan
"""

import pymongo
import sys
import getpass
import pprint

# Step 1
print ("Welcome to Vendor Profiling System\n")
client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")

# Step 2

while True:
    print ("Please enter the password\n")
    password = getpass.getpass()
    
    if password == "123456789":
        print("\nWelcome\n")
        break
    else:
        print("Wrong password please try again\n")
  
# Step 3
while True:
    db = (client.list_database_names())
    
    for list0 in range(0, len(db)):
        print (db[list0])
        
    array1 = ["Name","Institution","Designation","Email","Contact"]
    array2 = ["Name","Company","Designation","Email","Contact"]
    array3 = ["Company","Type","Address","E-Mail","Phone Number","Fax Number"]
    
    database = input("\nPlease Choose The Database (If want to quit the type [quit])\n")
    print ("")
    
    if database == "AfterMarketMARii":
        while True:
            db1 = client[database]
            col1 = db1.list_collection_names()
            for list1 in range(0, len(col1)):
                print (col1[list1])
            
            print(type(col1))
            collection1 = input("\nPlease Choose Type of Collection (type [back] to previous option)\n")
            print ("")
            
            if collection1 == "Academic":
                while True:
                    mycol1 = db1[collection1]
                    
                    for y1 in range(0, len(array1)):
                        print (array1[y1])

                    while True: 
                        parameter1 = input ("Please select the parameter: (type [all] to show all document)\n")
                        print ("")
                        
                        if parameter1 == "all":
                            query1 = None
                            break
                            
                        elif parameter1 in array1:
                            value1 = input(f"Please insert the {parameter1}\n")
                            value1ex = f"^{value1}"
                            valuex1 = {'$regex':value1ex,'$options': 'i'}
                            query1 = {parameter1:valuex1}
                            break

                        else:
                            print ("\nInvalid Input")
                            pass
                            
                    for x1 in mycol1.find(query1):
                        print("")
                        pprint.pprint(x1)
                        print("")
                        
                        
                    total1 = mycol1.count(query1)
                    print ("")
                    print ("total document is",total1)
                    decide1 = input("\nDo you want to find a new search in this collection? [Yes/No]\n")
                    
                    if decide1 == "Yes":
                        pass
                        
                    else:
                        print ("Okay\n")
                        break

                    
            elif collection1 in col1:
                while True:
                    
                    mycol1 = db1[collection1]
                    
                    for y1 in range(0, len(array2)):
                        print (array2[y1])
                    while True:
                        print("")
                        parameter1 = input ("Please select the parameter: (type [all] to show all document)\n")
                        print ("")
                        
                        if parameter1 == "all":
                            query1 = None
                            break
                            
                        elif parameter1 == "Name":
                            value1 = input(f"Please insert the {parameter1}\n")
                            value1ex = f"^{value1}"
                            valuex1 = {'$regex':value1ex,'$options': 'i'}
                            query1 = {parameter1:valuex1}
                            break
                        
                        elif parameter1 == "Company":
                            value1 = input(f"Please insert the {parameter1}\n")
                            value1ex = f"^{value1}"
                            valuex1 = {'$regex':value1ex,'$options': 'i'}
                            query1 = {parameter1:valuex1}
                            break
                        
                        elif parameter1 == "Designation":
                            value1 = input(f"Please insert the {parameter1}\n")
                            value1ex = f"^{value1}"
                            valuex1 = {'$regex':value1ex,'$options': 'i'}
                            query1 = {parameter1:valuex1}
                            break
                            
                        elif parameter1 == "Email":
                            value1 = input(f"Please insert the {parameter1}\n")
                            value1ex = f"^{value1}"
                            valuex1 = {'$regex':value1ex,'$options': 'i'}
                            query1 = {parameter1:valuex1}
                            break
                            
                        elif parameter1 == "Contact":
                            value1 = input(f"Please insert the {parameter1}\n")
                            value1ex = f"^{value1}"
                            valuex1 = {'$regex':value1ex,'$options': 'i'}
                            query1 = {parameter1:valuex1}
                            break
                            
                        else:
                            print ("\nInvalid Input")
                            pass
                            
                    for x1 in mycol1.find(query1):
                        print("")
                        pprint.pprint(x1)
                        
                        
                    total1 = mycol1.count(query1)
                    print ("")
                    print ("total document is",total1)
                    decide1 = input("\nDo you want to find a new search in this collection? [Yes/No]\n")
                    print("")
                    
                    if decide1 == "Yes":
                        pass
                        
                    else:
                        print ("Okay\n")
                        break

            
            elif collection1 == "back":
                break
            
            else:
                print ("\nThe Collection is not exist.\n")
    
    elif database == "ManufactureMARii":
        while True:
            
            db2 = client[database]
            col2 = db2.list_collection_names()
            for list2 in range(0, len(col2)):
                print (col2[list2])
                
            collection2 = input("\nPlease Choose Type of Collection (type [back] for previous option\n")
            
            if collection2 in col2:
                while True:
                    
                    mycol2 = db2[collection2]
                    
                    for y2 in range(0, len(array3)):
                        print (array3[y2])
                        
                    while True: 
                        print("")
                        parameter2 = input ("Please select the parameter: (type [all] to show all document)\n")
                        print ("")
                        
                        if parameter2 == "all":
                            query2 = None
                            break
                            
                        elif parameter2 in array3:
                            value2 = input(f"Please insert the {parameter2}\n")
                            value2ex = f"^{value2}"
                            valuex2 = {'$regex':value2ex,'$options': 'i'}
                            query2 = {parameter2:valuex2}
                            break

                        else:
                            print ("\nInvalid Input")
                            pass
                            
                    for x2 in mycol2.find(query2):
                        print("")
                        pprint.pprint(x2)
                        print("")
                        
                        
                    total2 = mycol2.count(query2)
                    print ("")
                    print ("total document is",total2)
                    decide2 = input("\nDo you want to find a new search in this collection? [Yes/No]\n")
                    print("")
                    
                    if decide2 == "Yes":
                        pass
                        
                    else:
                        print ("Okay\n")
                        break
                        
            elif collection2 =="back":
                break
            
            else:
                print ("\nThe Collection is not exist.\n")
                pass
            
    elif database == "quit":
        break
        sys.exit()
    else:
        print("Invalid Input\n")