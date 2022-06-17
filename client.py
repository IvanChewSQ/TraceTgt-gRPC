"""The Python implementation of the GRPC helloworld.Greeter client."""

from datetime import datetime
from __future__ import print_function
import logging
from mimetypes import init
import grpc

import Tracetogether_pb2, Tracetogether_pb2_grpc
class client:

def SetUsersData():
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')
    # create a stub (client)
    stub = Tracetogether_pb2_grpc.UserInfoStub(channel)
    #input data
    user_id  = int(input('Enter User Id : '))
    username = input('Enter Username : ')
    password = input('Enter Password : ')
    # create a valid request message
    data = Tracetogether_pb2.UserRequest(user_id=user_id,name=username,password=password)
    # make the call
    response = stub.Username(data)
    # response
    print(response.name)

def menu():
    print("[1] Individual Checkin/ Checkout")
    print("[2] Group Checkin/ Checkout")
    print("[3] Add Family Members into Group")
    print("[4] View History")
    print("[5] Declare Covid Clusters")
    print("[0] Exit Program")

if __name__ == '__main__':
    logging.basicConfig()
    SetUsersData()
    menu()

    while True:
        try:
            option = int(input("Enter an option: "))
            if option == "1":
                check_in = input("Enter your location:")
                print('You have Checked in at ' + check_in + ' at ' + str(datetime.now()))
                
                

            elif option == "2":
                print("Group Checkin/ Checkout Called\n")
                print('You have Checked out at'+ check_in + ' at ' + str(datetime.now()))

            elif option == "3":
                print("Add Family Members into Group Called\n")

            elif option == "4":
                print("View History Called\n")

            elif option == "5":
                print("Declare Covid Clusters Called\n")

            elif option == "0":
                print("End Program\n")
                exit()
            
            else:
                raise ValueError
        
        except ValueError:
            print("Enter an valid option!\n")