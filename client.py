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
    print("[5] Get History")
    print("[6] Check Cases")
    print("[7] Flag Cases")
    print("[0] Exit")


'''
    Check-in Functionality (Individual)
'''
def check_in(stub,name,nric,location):
    response = stub.check_in(Tracetogether_pb2.CheckIn_Request
        (name = name, nric = nric, location = location))
    print(response.message + "\n")


'''
Check-out Functionality (Individual)
'''
def check_out(stub,nric):
    response = stub.check_out(Tracetogether_pb2.CheckOut_Request
        (nric = nric))
    print(response.message + "\n")


'''
Check-in Functionality (Group)
'''
def check_in_grp(stub, nameList: list, nricList: list, location):
    response = stub.check_in_grp(Tracetogether_pb2.CheckIn_Grp_Request
        (name = nameList, nric = nricList, location = location))
    print(response.message + "\n")
"""    if type(nameList) != list or type(nricList) != list:
        print("Failure")
        return

    if len(nameList) != len(nricList):
        print("Failure")
        print("Number of names and nrics must be equal")
        return""" 

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
def get_history(stub,name,nric):
    response=stub.get_history(Tracetogether_pb2.Get_history_Request(name=name,nric=nric))
    print(response.message)

    for location in response.location:
        print(location)



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
                name = input("\nEnter Name: ")
                nric = input("Enter NRIC: ")
                location = input("Enter Location: ")
                check_in(stub, name, nric, location)
            
            elif choice == 2:
                nric = input("\nEnter NRIC: ")
                check_out(stub, nric)
            
            elif choice == 3:
                nameList = []
                nricList = []

                member = int(input("\nEnter number of family member (including yourself): "))
                i = 1
                while (i <= member):
                    print("\nDetails for member #",i)
                    name = input("Enter Name: ")
                    nric = input("Enter NRIC: ")
                    nameList.append(name)
                    nricList.append(nric)
                    i+=1
                location = input("\nEnter Location: ")
                check_in_grp(stub, nameList, nricList, location)
            
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

            elif choice == 0:
                exit()
            else:
                print("Invalid input\n")




