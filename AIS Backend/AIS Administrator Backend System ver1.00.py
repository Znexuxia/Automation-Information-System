"""
Created on Thu Jun  4 13:46:36 2020

Author: Shahazureen Ikwan
"""

import pymongo
import sys
import getpass
import pprint
import time

# Step 1
# Step 1
start = time.time()

try:
    
    print ("Welcome to Automotive Information System\n")
    client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false",serverSelectionTimeoutMS = 2000)
    client.server_info()
    
except:
    print("Connection Error\n")
    print(time.time() - start)
    sys.exit()


# Step 2
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

class security():
    while True:
        print ("Please enter the password\n")
        password = getpass.getpass()
        
        if password == "Administrator":
            print("\nWelcome\n")
            
            MESSAGE = b"Administrator"
        
            sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            sock.sendto(MESSAGE,(UDP_IP,UDP_PORT))
        
            break
        else:
            print("Wrong password please try again\n")

# Step 3
while True:
    class editorial():
        while True:
            option1 = ["Review","Edit"]
            option2 = ["Create", "Modify"]
        
            for a1 in range(0,len(option1)):
                print(option1[a1])
            
            choose1 = input("\nPlease choose what do you want to do with the database (type [quit] to exit system)\n")
            print ("")
            
            if choose1 == "Review":
                break
            
            elif choose1 == "quit":
                MESSAGE = b"Adminlogout"
        
                sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                sock.sendto(MESSAGE,(UDP_IP,UDP_PORT))
                sys.exit()
                
            elif choose1 == "Edit":
                while True:
                    print ("What do you want to edit with the database\n")
                    
                    for a2 in range(0, len(option2)):
                        print(option2[a2])
                        
                    choose2 = input("\nPlease type as option above to choose (type [back] to go to previous menu).\n")
                    
                    
                    if choose2 == "Create":
                        create1 = input ("Please type the database you want to create.\n")
                        mydb = client[create1]
                        print ("\nThe database is created")
                        
                        createcol1 = input ("Please type the collection name.\n")
                        mycol = mydb[createcol1]
                        rawdata = {}
                        mycol.insert_one(rawdata)
                        print ("\nThe collection is created.\n")
                        
                        MESSAGE = b"AdminADDdatabase"
        
                        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                        sock.sendto(MESSAGE,(UDP_IP,UDP_PORT))
                        
                        pass
                    
                    elif choose2 == "back":
                        print("")
                        break
                    
                    elif choose2 == "Modify":
                        while True:
                            db = (client.list_database_names())
                            
                            print("")
                            for list0 in range(0, len(db)):
                                print (db[list0])
               
                                
                            array1 = ["Name","Institution","Designation","Email","Contact"]
                            array2 = ["Name","Company","Designation","Email","Contact"]
                            array3 = ["Company","Type","Address","E-Mail","Phone Number","Fax Number"]
                            
                            database = input("\nPlease Choose The Database (If want to go back type [back])\n")
                            print ("")
                            
                            if database == "AfterMarketMARii":
                                while True:
                                    db1 = client[database]
                                    col1 = db1.list_collection_names()
                                    for list1 in range(0, len(col1)):
                                        print (col1[list1])
                            
                                    collection1 = input("\nPlease Choose Type of Collection (type [back] to previous option)\n")
                                    print ("")
                                    
                                    if collection1 == "Academic":
                                        while True:
                                            
                                            option3 = ["Add","Update","Delete"]
                                            option4 = ["Single","Multiple"]
                                            mycol1 = db1[collection1]
                                            for b1 in range(0, len(option3)):
                                                print(option3[b1])
                                                
                                            pick1 = input ("\nPlease type the action you want to do for this collection\n")
                                            print ("")
                                            
                                            if pick1 == "Add":
                 
                                                while True: 
                                                    for y1 in range(0, len(array1)):
                                                        print (array1[y1])
                                                    
                                                    parameter1 = input ("Please select the parameter: (type [done] to complete the modify)\n")
                                                    print ("")
                                                        
                                                    if parameter1 == "Name":
                                                        print ("")
                                                        key1 = "Name"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        while True:
                                                            if chose1 == "Single":
                                                                value1 = input(f"Please insert the {parameter1}\n")
                                                                value1ex = f"{value1}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = []
                                                                number = input ("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("PLease insert the element:\n")
                                                                    element_array.append(str(n))
                                                                print(element_array)
                                                                value1ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print ("Invalid input\n")
                                                                pass
                                                        
                                                    
                                                    elif parameter1 == "Institution":
                                                        print("")
                                                        key2 = "Institution"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("PLease choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value2 = input(f"Please insert the {parameter1}\n")
                                                                value2ex = f"{value2}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input ("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    element_array.append(str(n))
                                                                value2ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                        
                                                        print ("")
                                                        pass
                                                    
                                                    elif parameter1 == "Designation":
                                                        print("")
                                                        key3 = "Designation"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value3 = input(f"Please insert the {parameter1}\n")
                                                                value3ex = f"{value3}"
                                                                break
                                                            
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    element_array.append(str(n))
                                                                value3ex = element_array
                                                                break
                                                                
                                                            else:
                                                                print("Invaalid input\n")
                                                                pass
                                                            
                                                        print ("")
                                                        pass
                                                        
                                                    elif parameter1 == "Email":
                                                        print("")
                                                        key4 = "Email"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("PLease choose to set element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value4 = input(f"Please insert the {parameter1}\n")
                                                                value4ex = f"{value4}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("PLease insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value4ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                        
                                                        print ("")
                                                        pass
                                                        
                                                    elif parameter1 == "Contact":
                                                        print ("")
                                                        key5 = "Contact"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value5 = input(f"Please insert the {parameter1}\n")
                                                                value5ex = f"{value5}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value5ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                            
                                                        print ("")
                                                        pass
                                                        
                                                    elif parameter1 == "done":
                                                        query1 = {key1:value1ex,key2:value2ex,key3:value3ex,key4:value4ex,key5:value5ex}
                                                        break
                                                    
                                                    else:
                                                        print ("\nInvalid Input")
                                                        pass
                                                    
                                                x1 = mycol1.insert_one(query1)
                                                
                                                print ("Document Created")
                                                       
                                                decide1 = input("\nDo you want to continue create in this collection? [Yes/No]\n")
                                        
                                                if decide1 == "Yes":
                                                    pass
                                                    
                                                else:
                                                    print ("Okay\n")
                                                    break
                                                    
                                            elif pick1 == "Update":
                                                while True:
                                                    for y1 in range(0, len(array1)):
                                                        print (array1[y1])
                                                        
                                                        parameter1 = input ("Please select the parameter: (type [done] to complete the modify)\n")
                                                        print ("")
                                                            
                                                    if parameter1 in array1:
                                                        value1 = input(f"Please insert the {parameter1}\n")
                                                        value1ex = f"^{value1}"
                                                        valuex1 = {'$regex':value1ex,'$options': 'i'}
                                                        query1 = {parameter1:valuex1}
                                                        
                                                        for doc1 in mycol1.find(query1):
                                                            print("")
                                                            pprint.pprint(doc1)
                                                        print("")
                                                        
                                                        while True:
                                                            for g1 in range(0, len(option4)):
                                                                print(option4[g1])
                                                            chose1 = input("PLease choose to set element\n")
                                                            
                                                            if chose1 == "Single":
                                                        
                                                                newvalue1 = input(f"\nPlease insert to update the {parameter1}\n")
                                                                newquery1 = {'$set':{parameter1 : newvalue1}}
                                                                break
                                                            
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    element_array.append(str(n))
                                                                newvalue1 = element_array
                                                                newquery1 = {'$set':{parameter1 : newvalue1}}
                                                                break
                                                            
                                                            else:
                                                                print ("Invalid input\n")
                                                                pass
                                                                         
                                                        
                                                        else:
                                                            print ("Invalid Input")
                                                            pass
                                                        
                                                        x1 = mycol1.update_many(query1, newquery1)
                                                        print ("\nDocument Updated")
                                                               
                                                    decide1 = input("\nDo you want to create or modify in this collection? [Yes/No]\n")
                                            
                                                    if decide1 == "Yes":
                                                        pass
                                                        
                                                    else:
                                                        print ("Okay\n")
                                                        break
                        
                                            elif pick1 == "Delete":
                                                 while True:
                                                    for y1 in range(0, len(array1)):
                                                        print (array1[y1])
                                                        
                                                    parameter1 = input ("Please select the parameter: (type [back] to go previous menu.)\n")
                                                    print ("")
                                                        
                                                    if parameter1 in array1:
                                                        while True:
                                                            value1 = input(f"Please insert the {parameter1} (type [back] to go to previous option.)\n")
                                                            if value1 == "back":
                                                                break
                                                            
                                                            else:
                                                                value1ex = f"^{value1}"
                                                                valuex1 = {'$regex':value1ex,'$options': 'i'}
                                                                query1 = {parameter1:valuex1}
                                                                
                                                                for doc1 in mycol1.find(query1):
                                                                    print("")
                                                                    pprint.pprint(doc1)
                                                                print("")
                                                                
                                                                decide = input("Do you want to delete these document [Yes/No]?\n")
                                                                
                                                                if decide == "Yes":
                                                                    x1 = mycol1.delete_many(query1)
                                                    
                                                                    print (x1.deleted_count,"Document Deleted")
                                                                    break
                                                                
                                                                else:
                                                                    pass
                                                    
                                                    elif parameter1 == "back":
                                                        break
                                                    
                                                    else:
                                                        print ("Invalid Input")
                                                        pass
                                                        
                                                        
                                                        
                                                               
                                                    decide1 = input("\nDo you want to create or modify in this collection? [Yes/No]\n")
                                            
                                                    if decide1 == "Yes":
                                                        pass
                                                        
                                                    else:
                                                        print ("Okay\n")
                                                        break   
                                                    
                                    elif collection1 in col1:
                                        while True:
                                            
                                            option3 = ["Add","Update","Delete"]
                                            option4 = ["Single","Multiple"]
                                            mycol1 = db1[collection1]
                                            for b1 in range(0, len(option3)):
                                                print(option3[b1])
                                                
                                            pick1 = input ("Please type the action you want to do for this collection\n")
                                            print ("")
                                            
                                            if pick1 == "Add":
                 
                                                while True: 
                                                    for y1 in range(0, len(array2)):
                                                        print (array2[y1])
                                                    
                                                    parameter1 = input ("Please select the parameter: (type [done] to complete the modify)\n")
                                                    print ("")
                                                        
                                                    if parameter1 == "Name":
                                                        print ("")
                                                        key1 = "Name"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("PLease choose to set the element\n")
                                                        while True:
                                                            if chose1 == "Single":
                                                                value1 = input(f"Please insert the {parameter1}\n")
                                                                value1ex = f"{value1}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = []
                                                                number = input ("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("PLease insert the element:\n")
                                                                    element_array.append(str(n))
                                                                print(element_array)
                                                                value1ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print ("Invalid input\n")
                                                                pass
                                                        
                                                    
                                                    elif parameter1 == "Company":
                                                        print("")
                                                        key2 = "Company"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("PLease choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value2 = input(f"Please insert the {parameter1}\n")
                                                                value2ex = f"{value2}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input ("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    element_array.append(str(n))
                                                                value2ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                        
                                                        print ("")
                                                        pass
                                                    
                                                    elif parameter1 == "Designation":
                                                        print("")
                                                        key3 = "Designation"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value3 = input(f"Please insert the {parameter1}\n")
                                                                value3ex = f"{value3}"
                                                                break
                                                            
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    element_array.append(str(n))
                                                                value3ex = element_array
                                                                break
                                                                
                                                            else:
                                                                print("Invaalid input\n")
                                                                pass
                                                            
                                                        print ("")
                                                        pass
                                                        
                                                    elif parameter1 == "Email":
                                                        print("")
                                                        key4 = "Email"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("PLease choose to set element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value4 = input(f"Please insert the {parameter1}\n")
                                                                value4ex = f"{value4}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("PLease insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value4ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                        
                                                        print ("")
                                                        pass
                                                        
                                                    elif parameter1 == "Contact":
                                                        print ("")
                                                        key5 = "Contact"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value5 = input(f"Please insert the {parameter1}\n")
                                                                value5ex = f"{value5}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value5ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                            
                                                        print ("")
                                                        pass
                                                        
                                                    elif parameter1 == "done":
                                                        query1 = {key1:value1ex,key2:value2ex,key3:value3ex,key4:value4ex,key5:value5ex}
                                                        break
                                                    
                                                    else:
                                                        print ("\nInvalid Input")
                                                        pass
                                                    
                                                x1 = mycol1.insert_one(query1)
                                                
                                                print ("Document Created")
                                                       
                                                decide1 = input("\nDo you want to continue create in this collection? [Yes/No]\n")
                                        
                                                if decide1 == "Yes":
                                                    pass
                                                    
                                                else:
                                                    print ("Okay\n")
                                                    break
                                                    
                                            elif pick1 == "Update":
                                                while True:
                                                    for y1 in range(0, len(array1)):
                                                        print (array1[y1])
                                                        
                                                        parameter1 = input ("Please select the parameter: (type [done] to complete the modify)\n")
                                                        print ("")
                                                            
                                                    if parameter1 in array1:
                                                        value1 = input(f"Please insert the {parameter1}\n")
                                                        value1ex = f"^{value1}"
                                                        valuex1 = {'$regex':value1ex,'$options': 'i'}
                                                        query1 = {parameter1:valuex1}
                                                        
                                                        for doc1 in mycol1.find(query1):
                                                            print("")
                                                            pprint.pprint(doc1)
                                                        print("")
                                                        
                                                        while True:
                                                            for g1 in range(0, len(option4)):
                                                                print(option4[g1])
                                                            chose1 = input("PLease choose to set element\n")
                                                            
                                                            if chose1 == "Single":
                                                        
                                                                newvalue1 = input(f"\nPlease insert to update the {parameter1}\n")
                                                                newquery1 = {'$set':{parameter1 : newvalue1}}
                                                                break
                                                            
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    element_array.append(str(n))
                                                                newvalue1 = element_array
                                                                newquery1 = {'$set':{parameter1 : newvalue1}}
                                                                break
                                                            
                                                            else:
                                                                print ("Invalid input\n")
                                                                pass
                                                                         
                                                        
                                                        else:
                                                            print ("Invalid Input")
                                                            pass
                                                        
                                                        x1 = mycol1.update_many(query1, newquery1)
                                                        print ("\nDocument Updated")
                                                               
                                                    decide1 = input("\nDo you want to create or modify in this collection? [Yes/No]\n")
                                            
                                                    if decide1 == "Yes":
                                                        pass
                                                        
                                                    else:
                                                        print ("Okay\n")
                                                        break
                        
                                            elif pick1 == "Delete":
                                                 while True:
                                                    for y1 in range(0, len(array1)):
                                                        print (array1[y1])
                                                        
                                                    parameter1 = input ("Please select the parameter: (type [back] to go previous menu.)\n")
                                                    print ("")
                                                        
                                                    if parameter1 in array1:
                                                        while True:
                                                            value1 = input(f"Please insert the {parameter1} (type [back] to go to previous option.)\n")
                                                            if value1 == "back":
                                                                break
                                                            
                                                            else:
                                                                value1ex = f"^{value1}"
                                                                valuex1 = {'$regex':value1ex,'$options': 'i'}
                                                                query1 = {parameter1:valuex1}
                                                                
                                                                for doc1 in mycol1.find(query1):
                                                                    print("")
                                                                    pprint.pprint(doc1)
                                                                print("")
                                                                
                                                                decide = input("Do you want to delete these document [Yes/No]?\n")
                                                                
                                                                if decide == "Yes":
                                                                    x1 = mycol1.delete_many(query1)
                                                    
                                                                    print (x1.deleted_count,"Document Deleted")
                                                                    break
                                                                
                                                                else:
                                                                    pass
                                                    
                                                    elif parameter1 == "back":
                                                        break
                                                    
                                                    else:
                                                        print ("Invalid Input")
                                                        pass
                                                        
                                                        
                                                        
                                                               
                                                    decide1 = input("\nDo you want to create or modify in this collection? [Yes/No]\n")
                                            
                                                    if decide1 == "Yes":
                                                        pass
                                                        
                                                    else:
                                                        print ("Okay\n")
                                                        break
                                                  
                            elif database == "ManufactureMARii":
                                while True:
                                    
                                    db2 = client[database]
                                    col2 = db2.list_collection_names()
                                    for list2 in range(0, len(col2)):
                                        print (col2[list2])
                                        
                                    collection2 = input("\nPlease Choose Type of Collection (type [back] for previous option\n")
                                    print ("")
                                    
                                    if collection2 in col2:
                                        while True:
                                            
                                            option3 = ["Add","Update","Delete"]
                                            option4 = ["Single","Multiple"]
                                            mycol2 = db2[collection2]
                                            for b1 in range(0, len(option3)):
                                                print(option3[b1])
                                                
                                            pick1 = input ("\nPlease type the action you want to do for this collection\n")
                                            print ("")
                                            
                                            if pick1 == "Add":
                 
                                                while True: 
                                                    for y1 in range(0, len(array3)):
                                                        print (array3[y1])
                                                    
                                                    parameter1 = input ("\nPlease select the parameter: (type [done] to complete the modify)\n")
                                                    print ("")
                                                        
                                                    if parameter1 == "Company":
                                                        print ("")
                                                        key1 = "Company"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("PLease choose to set the element\n")
                                                        while True:
                                                            if chose1 == "Single":
                                                                value1 = input(f"Please insert the {parameter1}\n")
                                                                value1ex = f"{value1}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = []
                                                                number = input ("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("PLease insert the element:\n")
                                                                    element_array.append(str(n))
                                                                print(element_array)
                                                                value1ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print ("Invalid input\n")
                                                                pass
                                                        
                                                    
                                                    elif parameter1 == "Type":
                                                        print("")
                                                        key2 = "Type"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("PLease choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value2 = input(f"Please insert the {parameter1}\n")
                                                                value2ex = f"{value2}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input ("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    element_array.append(str(n))
                                                                value2ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                        
                                                        print ("")
                                                        pass
                                                    
                                                    elif parameter1 == "Address":
                                                        print("")
                                                        key3 = "Address"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value3 = input(f"Please insert the {parameter1}\n")
                                                                value3ex = f"{value3}"
                                                                break
                                                            
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    element_array.append(str(n))
                                                                value3ex = element_array
                                                                break
                                                                
                                                            else:
                                                                print("Invaalid input\n")
                                                                pass
                                                            
                                                        print ("")
                                                        pass
                                                        
                                                    elif parameter1 == "E-mail":
                                                        print("")
                                                        key4 = "E-mail"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("PLease choose to set element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value4 = input(f"Please insert the {parameter1}\n")
                                                                value4ex = f"{value4}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("PLease insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value4ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                        
                                                        print ("")
                                                        pass
                                                        
                                                    elif parameter1 == "Phone Number":
                                                        print ("")
                                                        key5 = "Phone Number"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value5 = input(f"Please insert the {parameter1}\n")
                                                                value5ex = f"{value5}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value5ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                            
                                                        print ("")
                                                        pass
                                                    
                                                    elif parameter1 == "Fax Number":
                                                        print ("")
                                                        key5 = "Fax Number"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value5 = input(f"Please insert the {parameter1}\n")
                                                                value5ex = f"{value5}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value5ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                            
                                                        print ("")
                                                        pass
                                                        
                                                    elif parameter1 == "H/P Number":
                                                        print ("")
                                                        key5 = "H/P Number"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value5 = input(f"Please insert the {parameter1}\n")
                                                                value5ex = f"{value5}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value5ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                        
                                                        print ("")
                                                        pass
                                                        
                                                    
                                                    elif parameter1 == "Name":
                                                        print ("")
                                                        key5 = "Name"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value5 = input(f"Please insert the {parameter1}\n")
                                                                value5ex = f"{value5}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value5ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                            
                                                        print ("")
                                                        pass
                                                        
                                                    elif parameter1 == "Position":
                                                        print ("")
                                                        key5 = "Position"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value5 = input(f"Please insert the {parameter1}\n")
                                                                value5ex = f"{value5}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value5ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                    
                                                    elif parameter1 == "Remark":
                                                        print ("")
                                                        key5 = "Remark"
                                                        for g1 in range(0, len(option4)):
                                                            print(option4[g1])
                                                        chose1 = input("Please choose to set the element\n")
                                                        
                                                        while True:
                                                            if chose1 == "Single":
                                                                value5 = input(f"Please insert the {parameter1}\n")
                                                                value5ex = f"{value5}"
                                                                break
                                                                
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    connect1 = element_array.append(str(n))
                                                                value5ex = element_array
                                                                break
                                                            
                                                            else:
                                                                print("Invalid input\n")
                                                                pass
                                                      
                                                    elif parameter1 == "done":
                                                        query1 = {key1:value1ex,key2:value2ex,key3:value3ex,key4:value4ex,key5:value5ex}
                                                        break
                                                    
                                                    else:
                                                        print ("\nInvalid Input")
                                                        pass
                                                    
                                                x1 = mycol2.insert_one(query1)
                                                
                                                print ("Document Created")
                                                       
                                                decide1 = input("\nDo you want to continue create in this collection? [Yes/No]\n")
                                        
                                                if decide1 == "Yes":
                                                    pass
                                                    
                                                else:
                                                    print ("Okay\n")
                                                    break
                                                    
                                            elif pick1 == "Update":
                                                while True:
                                                    for y1 in range(0, len(array1)):
                                                        print (array1[y1])
                                                        
                                                    parameter1 = input ("Please select the parameter: (type [done] to complete the modify)\n")
                                                    print ("")
                                                            
                                                    if parameter1 in array1:
                                                        value1 = input(f"Please insert the {parameter1}\n")
                                                        value1ex = f"^{value1}"
                                                        valuex1 = {'$regex':value1ex,'$options': 'i'}
                                                        query1 = {parameter1:valuex1}
                                                        
                                                        for doc2 in mycol2.find(query1):
                                                            print("")
                                                            pprint.pprint(doc2)
                                                        print("")
                                                        
                                                        while True:
                                                            for g1 in range(0, len(option4)):
                                                                print(option4[g1])
                                                            chose1 = input("PLease choose to set element\n")
                                                            
                                                            if chose1 == "Single":
                                                        
                                                                newvalue1 = input(f"\nPlease insert to update the {parameter1}\n")
                                                                newquery1 = {'$set':{parameter1 : newvalue1}}
                                                                break
                                                            
                                                            elif chose1 == "Multiple":
                                                                element_array = list()
                                                                number = input("Please set the number of element\n")
                                                                for i in range(int(number)):
                                                                    n = input("Please insert the element:\n")
                                                                    element_array.append(str(n))
                                                                newvalue1 = element_array
                                                                newquery1 = {'$set':{parameter1 : newvalue1}}
                                                                break
                                                            
                                                            else:
                                                                print ("Invalid input\n")
                                                                pass
                                                                         
                                                        
                                                        else:
                                                            print ("Invalid Input")
                                                            pass
                                                        
                                                        x1 = mycol1.update_many(query1, newquery1)
                                                        print ("\nDocument Updated")
                                                               
                                                    decide1 = input("\nDo you want to create or modify in this collection? [Yes/No]\n")
                                            
                                                    if decide1 == "Yes":
                                                        pass
                                                        
                                                    else:
                                                        print ("Okay\n")
                                                        break
                        
                                            elif pick1 == "Delete":
                                                 while True:
                                                    for y1 in range(0, len(array1)):
                                                        print (array1[y1])
                                                        
                                                    parameter1 = input ("Please select the parameter: (type [back] to go previous menu.)\n")
                                                    print ("")
                                                        
                                                    if parameter1 in array1:
                                                        while True:
                                                            value1 = input(f"Please insert the {parameter1} (type [back] to go to previous option.)\n")
                                                            if value1 == "back":
                                                                break
                                                            
                                                            else:
                                                                value1ex = f"^{value1}"
                                                                valuex1 = {'$regex':value1ex,'$options': 'i'}
                                                                query1 = {parameter1:valuex1}
                                                                
                                                                for doc1 in mycol1.find(query1):
                                                                    print("")
                                                                    pprint.pprint(doc1)
                                                                print("")
                                                                
                                                                decide = input("Do you want to delete these document [Yes/No]?\n")
                                                                
                                                                if decide == "Yes":
                                                                    x1 = mycol1.delete_many(query1)
                                                    
                                                                    print (x1.deleted_count,"Document Deleted")
                                                                    break
                                                                
                                                                else:
                                                                    pass
                                                    
                                                    elif parameter1 == "back":
                                                        break
                                                    
                                                    else:
                                                        print ("Invalid Input")
                                                        pass
                                                        
                                                        
                                                        
                                                               
                                                    decide1 = input("\nDo you want to create or modify in this collection? [Yes/No]\n")
                                            
                                                    if decide1 == "Yes":
                                                        pass
                                                        
                                                    else:
                                                        print ("Okay\n")
                                                        break
                            
      
    # Step 4
    class reference():
        while True:
            db = (client.list_database_names())
            
            for list0 in range(0, len(db)):
                print (db[list0])
                
            array1 = ["Name","Institution","Designation","Email","Contact"]
            array2 = ["Name","Company","Designation","Email","Contact"]
            array3 = ["Company","Type","Address","E-Mail","Phone Number","Fax Number"]
            
            database = input("\nPlease Choose The Database (If want to go previous menu the type [back])\n")
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
                    
            elif database == "back":
                break
                
            else:
                print("Invalid Input\n")