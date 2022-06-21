from datetime import datetime
import logging
import grpc
import re
import Tracetogether_pb2 as Tracetogether_pb2, Tracetogether_pb2_grpc as Tracetogether_pb2_grpc


"""
    Regex for User Input
"""
date_regex = re.compile(r"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$")
time_regex = re.compile(r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$")


"""
    Menu Selection for User
"""
def menu():
    print("\n[1] Declare COVID-19 visited locations")
    print("[2] Diaplay all details of COVID-19 visited locations")
    print("[3] View all potential affected users")
    print("[0] Exit")


"""
    Function to get Date input and check 
"""
def checkDate():
    while True:
        date = input("Enter Date (YYYY-MM-DD): ")
        if re.search(date_regex, date):
            if date <= str(datetime.now()):
                return date
            else:
                print("Invalid Date, please enter a date in the past")
        else: 
            print("Invalid Date format, please follow the format of (YYYY-MM-DD)")


"""
    Function to get Time input and check 
"""
def checkTime():
    while True:
        time = input("Enter Time (HH:MM): ")
        if re.match(time_regex, time):
            if time <= str(datetime.now().strftime("%H:%M")):
                return time
            else:
                print("Invalid Time, please enter a time in the past")
        else:
             print("Invalid Time format, please follow the format of (HH:MM)")


'''
    Function to declare COVID-19 location
    1. Request date, time and location from users
    2. Send notification to affected users
'''
def declare_location(stub):
    location = input("\nEnter Location: ")
    date = checkDate()
    time = checkTime()
    response = stub.check_in(Tracetogether_pb2.Declare_Request
        (date = date, time = time, location = location))
    print(response.message + "\n")


if __name__ == '__main__':
    logging.basicConfig()
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = Tracetogether_pb2_grpc.TracetogetherStub(channel)
        while True:
            try:
                menu()
                choice = int(input("Enter an option: "))

                if choice == 1:
                    declare_location(stub)
                
                elif choice == 2:
                    pass
                
                elif choice == 0:
                    exit()

                else:
                    print("Invalid input, please try again\n")
                    continue

            except ValueError:
                print("Invalid Value, please try again\n")
                continue