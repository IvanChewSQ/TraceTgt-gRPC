from datetime import datetime
import logging
from mimetypes import init
import grpc
import re
import Tracetogether_pb2 as Tracetogether_pb2, Tracetogether_pb2_grpc as Tracetogether_pb2_grpc

"""
    Regex for User Input
"""
name_regex = re.compile(r"[A-Za-z]+")
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
    print("[0] Exit")


"""
    Function to get Name Input and check 
"""
def checkName():
    while True:
        name = input("\nEnter Name: ").upper()
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
def check_in(stub):
    name = checkName()
    nric = checkNric()
    location = input("Enter Location: ").upper()
    response = stub.check_in(Tracetogether_pb2.CheckIn_Request
        (name = name, nric = nric, location = location))
    print(response.message + "\n")


'''
    (Individual) Check-out Functionality 
    1. Request nric from users for search in database
    2. Trigger gRPC to server for checkout
    3. Display server output 
'''
def check_out(stub):
    nric = checkNric()
    response = stub.check_out(Tracetogether_pb2.CheckOut_Request
        (nric = nric))
    print(response.message + "\n")


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
        print("\nDetails for member #", i)
        name = checkName()
        nric = checkNric()
        nameList.append(name)
        nricList.append(nric)
        i+=1
    location = input("\nEnter Location: ").upper()
    response = stub.check_in_grp(Tracetogether_pb2.CheckIn_Grp_Request
        (name = nameList, nric = nricList, location = location))
    print(response.message + "\n")

    
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
        print("\nDetails for member #", i)
        nric = checkNric()
        nricList.append(nric)
        i+=1
    response = stub.check_out_grp(Tracetogether_pb2.CheckOut_Grp_Request
        (nric = nricList))
    print(response.message + "\n")


'''
    Get History Functionality
    1. Request nric from users
    2. Trigger gRPC to retrieve all history record associated with the nric
    3. Display output
'''
def get_history(stub):
    nric = checkNric()
    """
    response=stub.get_history(Tracetogether_pb2.History_Request
        (nric=nric))  

    history_list = ''   

    for word in response.history:
        history_list += str(word + "")
    history_list = history_list[:-1]
    history_list += '.'

    print("Your history for the past 14 days: \n", history_list)"""


    response = stub.get_history(Tracetogether_pb2.ViewLocation_Request(nric=nric))
    print("Your history for the past 14 days: \n", response.history)

def check_cases(stub,name,nric):
    response=stub.check_cases(Tracetogether_pb2.Check_cases_Request(name=name,nric=nric))
    print(response.message)

def flag_cases(stub,name,nric):
    response=stub.flag_cases(Tracetogether_pb2.Flag_cases_Request(name=name,nric=nric))
    print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Tracetogether_pb2_grpc.TracetogetherStub(channel)
        while True:
            try:
                menu()
                choice = int(input("Enter an option: "))

                if choice == 1:
                    check_in(stub)
                
                elif choice == 2:
                    check_out(stub)
                
                elif choice == 3:
                    check_in_grp(stub)
                
                elif choice == 4:
                    check_out_grp(stub)
                
                elif choice == 5:
                    get_history(stub)

                elif choice == 0:
                    exit()
                
                else:
                    print("Invalid input, please try again\n")
                    continue
                
            except ValueError:
                print("Invalid Value, please try again\n")
                continue