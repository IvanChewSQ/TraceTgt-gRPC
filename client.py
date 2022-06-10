"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging
from mimetypes import init
import grpc

import Tracetogether_pb2, Tracetogether_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = Tracetogether_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(Tracetogether_pb2.HelloRequest(name='Jeremy Chng'))
    print("Welcome to the Tracetogether Client! Connecting..." + response.message)

def menu():
    print("[1] Individual Checkin/ Checkout")
    print("[2] Group Checkin/ Checkout")
    print("[3] Add Family Members into Group")
    print("[4] View History")
    print("[5] Declare Covid Clusters")
    print("[0] Exit Program")

if __name__ == '__main__':
    logging.basicConfig()
    run()
    menu()

    while True:
        try:
            option = int(input("Enter an option: "))
            if option == 1:
                print("Individual Checkin/ Checkout Called\n")

            elif option == 2:
                print("Group Checkin/ Checkout Called\n")

            elif option == 3:
                print("Add Family Members into Group Called\n")

            elif option == 4:
                print("View History Called\n")

            elif option == 5:
                print("Declare Covid Clusters Called\n")

            elif option == 0:
                print("End Program\n")
                exit()
            
            else:
                raise ValueError
        
        except ValueError:
            print("Enter an valid option!\n")