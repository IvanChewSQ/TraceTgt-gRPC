from datetime import datetime
import logging
import grpc
import re
import Tracetogether_pb2, Tracetogether_pb2_grpc


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
    print("[2] Display all details of COVID-19 visited locations")
    print("[3] Remove COVID-19 visited locations")
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
def checkTime(date):
    while True:
        time = input("Enter Time (HH:MM): ")
        if re.match(time_regex, time):
            if (date == datetime.now().strftime("%Y-%m-%d")):
                if time <= str(datetime.now().strftime("%H:%M")):
                    return time
                else:
                    print("Invalid Time, please enter a time in the past")
            else:
                return time
        else:
             print("Invalid Time format, please follow the format of (HH:MM)")


'''
    Function to declare COVID-19 location
    1. Request date, time and location from users
'''
def declare_location(stub):
    print()
    location = input("Enter Location: ").upper()
    date = checkDate()
    time = checkTime(date)
    response = stub.delcare_locations(Tracetogether_pb2.Declare_Request
        (location = location, date = date, time = time))
    print(response.message + "\n")
    print("Notification will be sent to the affected users")


'''
    Function to view all declared COVID-19 location with the number of days 
        with respect from the date it was being declared to today
'''
def view_location(stub):
    print()
    response = stub.view_locations(Tracetogether_pb2.ViewLocation_Request())
    print("Declared COVID-19 locations: \n", response.location)


'''
    Function to remove selected declared COVID-19 location 
'''
def remove_location(stub):
    print()
    location = input("Enter Location to remove: ").upper()
    response = stub.remove_locations(Tracetogether_pb2.RemoveLocation_Request
        (location = location))            
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
                    declare_location(stub)
                
                elif choice == 2:
                    view_location(stub)
                
                elif choice == 3:
                    remove_location(stub)

                elif choice == 0:
                    exit()

                else:
                    print("Invalid input, please try again\n")
                    continue

            except ValueError:
                print("Invalid Value, please try again\n")
                continue
            