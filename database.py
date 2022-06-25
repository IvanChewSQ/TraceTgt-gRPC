from asyncio.windows_events import NULL
from cmath import inf
import json
from datetime import timedelta, datetime
from numpy import append

from sqlalchemy import false

class Database():
    
    """
        Initialise and open the file in read mode
    """
    def __init__(self):
        self.data_file = json.load(open("data/data.json", "r"))
        self.cluster_file = json.load(open("data/cluster.json", "r"))


    """
        Function to add new SafeEntry details into data.json
        Parameters: name, nric, location, checkin datetime, checkout datetime
    """
    def addDetails(self, name, nric, location, checkin_time, checkout_time):
        ID = 0 + len(self.data_file)
        data = {
            ID: [
                {
                    "nric": nric,
                    "name": name,
                    "location": location,
                    "checkInDateTime": checkin_time,
                    "checkOutDateTime": checkout_time,
                    "ID": ID
                }
            ]
        }
        self.data_file.update(data)
        json_obj = json.dumps(self.data_file, indent=4)
        with open("data/data.json", "w") as out:
            out.write(json_obj)


    """
        Function to tally nric and update existing SafeEntry details 
            with the check out datetime
        Parameters: nric, checkout datetime
    """
    def updateDetails(self, nric, dateTime):
        ID = 0 + len(self.data_file)-1 # get last ID
        for ID, value in self.data_file.items():    # loop through all the items in the dictionary
            for i in value:                    # loop through all the items in the list
                if i["nric"] == nric and i["checkOutDateTime"] == "": # if nric matches with the nric in the list and check out datetime is not empty
                    i["checkOutDateTime"] = dateTime

        json_obj = json.dumps(self.data_file, indent=4)
        with open("data/data.json", "w") as out:
            out.write(json_obj)


    """
        Function to get list of locations visited by user
        Parameters: nric
    """
    def getHistory(self, nric):
        history_list = []    # list of dictionaries

        for ID, value in self.data_file.items():   # loop through all the items in the dictionary
            for i in value:
                if i["nric"] == nric:
                    history_list.append("Location: "+ i["location"] +", Checkin: " +
                        i["checkInDateTime"] +", Checkout : " + i["checkOutDateTime"])

        return history_list


    """
        Function to set Covid19 visited location
        Parameters: location, date, time
    """
    def set_covidLocation(self, location, date, time):
        ID = 0 + len(self.cluster_file)-1
        if ID in self.cluster_file :  # if the ID is already in the dictionary
            print("ID is already in use, incrementing index...")   
            ID +=1
        else:                 # increment the ID
            data = {
                ID: [
                    {
                        "cluster_location": location,
                        "date": date,
                        "time": time,
                        "ID": ID
                    }
                ]
            }
            self.cluster_file.update(data)
            json_obj = json.dumps(self.cluster_file, indent=4)
            with open("data/cluster.json", "w") as out:
                out.write(json_obj)
            

    """
        Function to view all declared Covid-19 Locations with the number of days 
            with respect from the date it was being declared to today
    """
    def view_covidLocation(self):
        location_list = []
        ID = 0 + len(self.data_file)-1 # get last ID
        today = datetime.strptime(str(datetime.now().date()), "%Y-%m-%d")

        for ID, value in self.cluster_file.items():   # loop through all the items in the dictionary
            for i in value:
                date = datetime.strptime(i["date"],"%Y-%m-%d")
                delta = today - date
                location_list.append(i["cluster_location"] + " - Day "+str(delta.days))
                
        return location_list

    """
        Function to remove declared Covid-19 Locations
        Parameters: location
    """
    def remove_covidLocation(self, location):
        for ID, value in self.cluster_file.items():    # loop through all the items in the dictionary
            for i in value: 
                if i["cluster_location"] == location:   # if the location is found
                    del self.cluster_file[ID]   # remove the location from the dictionary
                    json_obj = json.dumps(self.cluster_file, indent=4)
                    with open("data/cluster.json", "w") as out:
                        out.write(json_obj)
                    return True

    '''Function to check if user has visited an infected location within past 14 days
    Args: nric of user and list of infected locations
    Returns TODO'''
    def notify_covid_location(self, nric):
        today = datetime.strptime(str(datetime.now().date()), "%Y-%m-%d")
        infected_list=[]
        ID = 0 + len(self.cluster_file)-1   # get last ID
        for ID, value in self.data_file.items():   # loop through all the items in the data.json dictionary
            for i in value: 
                if i["nric"] == nric:   # if the nric is found
                    for ID, value in self.cluster_file.items():  # loop through all the items in the cluster.json dictionary
                        for i in value: # loop through all the items in the list
                            date = datetime.strptime(i["date"],"%Y-%m-%d")  # convert date to datetime
                            delta = today - date                            
                            if delta.days <= 0:                            
                                if i["cluster_location"] == self.data_file[ID][0]["location"]:  # if the location is the same as the location in the data.json
                                    infected_list.append(i["location"]+ " - Days ago "+str(delta.days))
                                    print(infected_list)
                                    return infected_list


        # LocationList = []

        # now = datetime.now()
        # cur = now - timedelta(days=14)
      
        # visitedLocation = self.data_file[nric]  # get the list of visited locations
        # for j in visitedLocation:   # loop through all the items in the list
        #     locations = j["location"]
        #     locationDateTime = j["checkInDateTime"]
        #     locationDateTime = datetime.strptime(locationDateTime, '%d/%m/%Y, %H:%M:%S')

        #     if locationDateTime > cur and locations in infectedLocation:    # if the location is visited within past 14 days and is in the list of infected locations
        #         locationDateTime = datetime.strftime(locationDateTime, '%d/%m/%Y, %H:%M:%S')
        #         LocationList.append(locations)  # add the location to the list
        #         LocationList.append(locationDateTime)   # add the date and time to the list
    

        # print(LocationList) 
        # return LocationList # return the list of locations and date and time