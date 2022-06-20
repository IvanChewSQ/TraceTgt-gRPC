"""The Python implementation of the GRPC helloworld.Greeter client."""

from datetime import datetime
import logging
from mimetypes import init
import grpc

import Tracetogether_pb2 as Tracetogether_pb2, Tracetogether_pb2_grpc as Tracetogether_pb2_grpc

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
GRPC Client
'''

'''
Check-in Functionality (Individual)
'''
def check_in(stub,name,nric,location,check_in):
    response=stub.check_in(Tracetogether_pb2.Check_in_Request(name=name,nric=nric,location=location,check_in=check_in))
    print(response.message)


'''
Check-out Functionality (Individual)
'''
def check_out(stub,name,nric,location,check_out):
    response=stub.check_out(Tracetogether_pb2.Check_out_Request(name=name,nric=nric,location=location,check_out=check_out))
    print(response.message)

'''
Check-in Functionality (Group)
'''
def check_in_grp(stub, nameList: list, nricList: list, location, check_in):
    if type(nameList) != list or type(nricList) != list:
        print("Failure")
        print("Input must be input in a list E.g. [\"Ivan\",\"Jeremy\"] or [\"Sxxxxxx\",\"Sxxxxxx\"]")
        return

    if len(nameList) != len(nricList):
        print("Failure")
        print("Number of names and nrics must be equal")
        return

    response=stub.check_in_grp(Tracetogether_pb2.Check_in_grp_Request
    (name=nameList,nric=nricList,location=location,check_in=check_in))
    print(response.message)


'''
Check-out Functionality (Group)
'''
def check_out_grp(stub, nameList: list, nricList: list, location, check_out):
    if type(nameList) != list or type(nricList) != list:
        print("Failure")
        print("Input must be input in a list E.g. [\"Ivan\",\"Jeremy\"] or [\"Sxxxxxx\",\"Sxxxxxx\"]")
        return

    if len(nameList) != len(nricList):
        print("Failure")
        print("Number of names and nrics in the list must be equal")
        return

    response=stub.check_out_grp(Tracetogether_pb2.Check_out_grp_Request
    (name=nameList,nric=nricList,location=location,check_out=check_out))
    print(response.message)

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
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    logging.basicConfig()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Tracetogether_pb2_grpc.TracetogetherStub(channel)
        '''
    [1] Individual Check In
    [2] Individual Check Out
    [3] Group Check In
    [4] Group Check Out
    [5] Get History
    [6] Check Cases
    [7] Flag Cases
    [0] Exit
        '''
        while True:
            menu()
            choice = int(input())
            if choice == 1:
                name = input("Enter name: ")
                nric = input("Enter nric: ")
                location = input("Enter location: ")
                check_in = get_time()
                check_in(stub,name,nric,location,check_in)

            elif choice == 2:
                name = input("Enter name: ")
                nric = input("Enter nric: ")
                location = input("Enter location: ")
                check_out = get_time()
                check_out(stub,name,nric,location,check_out)

            elif choice == 3:
                nameList = input("Enter name: ")
                nricList = input("Enter nric: ")
                location = input("Enter location: ")
                check_in = get_time()
                check_in_grp(stub,nameList,nricList,location,check_in)
            
            elif choice == 4:
                nameList = input("Enter name: ")
                nricList = input("Enter nric: ")
                location = input("Enter location: ")
                check_out = get_time()
                check_out_grp(stub,nameList,nricList,location,check_out)
            
            elif choice == 5:
                name = input("Enter name: ")
                nric = input("Enter nric: ")
                get_history(stub,name,nric)

            elif choice == 6:
                name = input("Enter name: ")
                nric = input("Enter nric: ")
                check_cases(stub,name,nric)

            elif choice == 7:
                name = input("Enter name: ")
                nric = input("Enter nric: ")
                flag_cases(stub,name,nric)

            elif choice == 0:
                exit()
            else:
                print("Invalid input")

        now = datetime.now()
        flag_location(stub, "Tekong", now.strftime("%d/%m/%Y, %H:%M:%S"))


