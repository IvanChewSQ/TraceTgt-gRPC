from datetime import datetime
import logging
from mimetypes import init
import grpc
import Tracetogether_pb2 as Tracetogether_pb2, Tracetogether_pb2_grpc as Tracetogether_pb2_grpc

"""
    Menu Selection for User
"""
def menu():
    print("[1] Individual Check In")
    print("[2] Individual Check Out")
    print("[3] Group Check In")
    print("[4] Group Check Out")
    print("[5] Retrieve Check In/Out History")
    print("[6] Check Cases")
    print("[7] Flag Cases")
    print("[0] Exit")


'''
    Check-in Functionality (Individual)
    1. Request name, nric, location from users
    2. Trigger gRPC to server for checkin
    3. Display server output
'''
def check_in(stub):
    name = input("\nEnter Name: ")
    nric = input("Enter NRIC: ")
    location = input("Enter Location: ")
    response = stub.check_in(Tracetogether_pb2.CheckIn_Request
        (name = name, nric = nric, location = location))
    print(response.message + "\n")


'''
    Check-out Functionality (Individual)
    1. Request nric from users for search in database
    2. Trigger gRPC to server for checkout
    3. Display server output 
'''
def check_out(stub):
    nric = input("\nEnter NRIC: ")
    response = stub.check_out(Tracetogether_pb2.CheckOut_Request
        (nric = nric))
    print(response.message + "\n")


'''
    Check-in Functionality (Group)
    1. Request the number of family members
    2. Request all the name, nric and location from users
    3. Trigger gRPC to server for group checkin
    3. Display server output
'''
def check_in_grp(stub):
    nameList = []
    nricList = []

    member = int(input("\nEnter number of family member (including yourself): "))
    i = 1
    while (i <= member):
        print("\nDetails for member #", i)
        name = input("Enter Name: ")
        nric = input("Enter NRIC: ")
        nameList.append(name)
        nricList.append(nric)
        i+=1
    location = input("\nEnter Location: ")
    response = stub.check_in_grp(Tracetogether_pb2.CheckIn_Grp_Request
        (name = nameList, nric = nricList, location = location))
    print(response.message + "\n")












'''
    Check-out Functionality (Group)
'''
def check_out_grp(stub, nricList: list):
    response = stub.check_out_grp(Tracetogether_pb2.CheckOut_Grp_Request
    (nric = nricList))
    print(response.message + "\n")
"""
    if type(nameList) != list or type(nricList) != list:
        print("Failure")
        return

    if len(nameList) != len(nricList):
        print("Failure")
        print("Number of names and nrics in the list must be equal")
        return"""


'''
    Get History Functionality
'''
def get_history(stub, nric):
    response=stub.get_history(Tracetogether_pb2.Get_history_Request
        (nric=nric))
    print(response.message + "\n")






def check_cases(stub,name,nric):
    response=stub.check_cases(Tracetogether_pb2.Check_cases_Request(name=name,nric=nric))
    print(response.message)

def flag_cases(stub,name,nric):
    response=stub.flag_cases(Tracetogether_pb2.Flag_cases_Request(name=name,nric=nric))
    print(response.message)


def get_time():
    now=datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


if __name__ == '__main__':
    logging.basicConfig()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Tracetogether_pb2_grpc.TracetogetherStub(channel)
        while True:
            menu()
            choice = int(input("Enter an option: "))

            if choice == 1:
                check_in(stub)
            
            elif choice == 2:
                check_out(stub)
            
            elif choice == 3:
                check_in_grp(stub)
            
            elif choice == 4:
                nricList = []

                member = int(input("\nEnter number of family member (including yourself): "))
                i = 1
                while (i <= member):
                    print("\nDetails for member #",i)
                    nric = input("Enter NRIC: ")
                    nricList.append(nric)
                    i+=1
                check_out_grp(stub, nricList)
            
            elif choice == 5:
                nric = input("\nEnter NRIC: ")
                get_history(stub, nric)

            elif choice == 0:
                exit()
            else:
                print("Invalid input\n")




