from datetime import datetime
import logging
from mimetypes import init
from queue import Empty
import grpc
import re
import sys
import Tracetogether_pb2, Tracetogether_pb2_grpc

"""
    Regex for User Input
"""
name_regex = re.compile(r"^[\-'a-zA-Z ]+$")
nric_regex = re.compile(r"(?i)^[STFG]\d{7}[A-Z]$")
    

"""
    Menu Selection for User
"""
def menu():
    print("\n[1] Individual Check In")
    print("[2] Individual Check Out")
    print("[3] Group Check In")
    print("[4] Group Check Out")
    print("[5] Retrieve Check In/Out History")
    print("[6] View Covid19 Declared Locations")
    print("[0] Exit")


"""
    Function to get Name Input and check 
"""
def checkName():
    while True:
        name = input("Enter Name: ").upper()
        if re.match(name_regex, name):
            return name
        else: 
            print("Invalid Name, please verify")


"""
    Function to get NRIC Input and check 
"""
def checkNric():
    while True:
        nric = input("Enter NRIC: ").upper()
        if re.match(nric_regex, nric):
            return nric
        else:
            print("Invalid NRIC, please verify")


'''
    (Individual) Check-in Functionality 
    1. Request name, nric, location from users
    2. Trigger gRPC to server for checkin
    3. Display server output
'''
def check_in(stub, nric):
    print()
    name = checkName()
    location = input("Enter Location: ").upper()
    response = stub.check_in(Tracetogether_pb2.CheckIn_Request
        (name = name, nric = nric, location = location))
    print(response.message)


'''
    (Individual) Check-out Functionality 
    1. Request nric from users for search in database
    2. Trigger gRPC to server for checkout
    3. Display server output 
'''
def check_out(stub, nric):
    print()
    response = stub.check_out(Tracetogether_pb2.CheckOut_Request
        (nric = nric))
    print(response.message)


'''
    (Group) Check-in Functionality 
    1. Request the number of family members
    2. Request all the name, nric and location from users
    3. Trigger gRPC to server for group checkin
    4. Display server output
'''
def check_in_grp(stub):
    nameList = []
    nricList = []

    while True:
        try: 
            member = int(input("\nEnter number of family member (including yourself): "))
        except ValueError:
            print("Invalid Value, please try again")
            continue
        else:
            break
    i = 1
    while (i <= member):
        while True:
            print() 
            print("Details for member #", i)
            name = checkName()
            nric = checkNric()
            if (nric not in nricList):
                nameList.append(name)
                nricList.append(nric)
                i+=1
                break
            else:
                i = 1
                nameList.clear()
                nricList.clear()
                print ("\nDuplicated NRIC, please check all input fields again")
        
    location = input("\nEnter Location: ").upper()
    response = stub.check_in_grp(Tracetogether_pb2.CheckIn_Grp_Request
        (name = nameList, nric = nricList, location = location))
    print(response.message)



'''
    (Group) Check-out Functionality 
    1. Request the number of family members
    2. Request all nric from users
    3. Trigger gRPC to server for group checkout
    4. Display server output
'''
def check_out_grp(stub):
    nricList = []
    while True:
        try: 
            member = int(input("\nEnter number of family member (including yourself): "))
        except ValueError:
            print("Invalid Value, please try again")
            continue
        else:
            break
    i = 1
    while (i <= member):
        while True: 
            print("\nDetails for member #", i)
            nric = checkNric()
            if (nric not in nricList):
                nricList.append(nric)
                i+=1
                break
            else:
                i = 1
                nricList.clear()
                print ("\nDuplicated NRIC, please check all input fields again")
    response = stub.check_out_grp(Tracetogether_pb2.CheckOut_Grp_Request
        (nric = nricList))
    print(response.message)


'''
    Get History Functionality
    1. Request nric from users
    2. Trigger gRPC to retrieve all history record associated with the nric
    3. Display output
'''
def get_history(stub, nric):
    print()
    response = stub.get_history(Tracetogether_pb2.History_Request(nric=nric))
    print("\nCheck In/Out History:",)
    for i in response.history:
        print(i, end = "\n")


'''
    Function to view all declared COVID-19 location with the number of days 
        with respect from the date it was being declared to today
'''
def view_location(stub):
    print()
    response = stub.view_locations(Tracetogether_pb2.ViewLocation_Request())
    print("Declared COVID-19 locations:")
    for i in response.location:
        print(i, end = "\n")


'''
    Notification function if user had checkin to a declared location for the past 14 days
'''
def notify_location(stub):
    print()
    response = stub.notify_covid_location(Tracetogether_pb2.Notify_Covid_Request
        (nric=nric))
    if response.message:
        print("********************************************* WARNING *********************************************")
        print("You had visited the following Covid-19 Locations in the past 14 days: \n")
        for i in response.message:
            print(i, end = "\n")
        print("***************************************************************************************************")


if __name__ == '__main__':
    nric = sys.argv[1]
    logging.basicConfig()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Tracetogether_pb2_grpc.TracetogetherStub(channel)
        while True:
            try:
                notify_location(stub)
                menu()
                choice = int(input("Enter an option: "))

                if choice == 1:
                    check_in(stub, nric)
                
                elif choice == 2:
                    check_out(stub,nric)
                
                elif choice == 3:
                    check_in_grp(stub)
                
                elif choice == 4:
                    check_out_grp(stub)
                
                elif choice == 5:
                    get_history(stub, nric)

                elif choice == 6:
                    view_location(stub)                   

                elif choice == 0:
                    exit()
                
                else:
                    print("Invalid input, please try again\n")
                    continue
                
            except ValueError:
                print("Invalid Value, please try again\n")
                continue