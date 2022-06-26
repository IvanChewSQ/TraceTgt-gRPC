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
        Function to check if user has visited an infected location within past 14 days
        Parameters: NRIC
    """   
    def notify_covid_location(self, nric):
        location=[]
        date=[]
        infected_list=[]
        for ID, value in self.cluster_file.items():
            for i in value: 
                location.append(i["cluster_location"]),
                date.append(i["date"])

        for ID, value in self.data_file.items():
            for i in value: 
                if i["nric"] == nric:
                    if i["location"] in location:
                        index = location.index(i["location"])
                        declaredate = datetime.strptime(date[index], "%Y-%m-%d")
                        startdate = declaredate - timedelta(13)
                        checkin = datetime.strptime(i["checkInDateTime"], "%Y-%m-%d %H:%M:%S")
                        if startdate.date() <= checkin.date() <= declaredate.date():
                            infected_list.append(i["location"] + " declared on " + date[index] + ". You had Check-In at "+ i["checkInDateTime"] + " and Check-Out at "+ i["checkOutDateTime"])
        return infected_list
        


        """
        infected_list=[]
        ID = 0 + len(self.cluster_file)-1   # get last ID
        for ID, value in self.data_file.items():   # loop through all the items in the data.json dictionary
            for i in value: 
                if i["nric"] == nric:   # if the nric is found
                    for ID, value in self.cluster_file.items():   # loop through all the items in the cluster.json dictionary
                        for j in value:
                            if j["cluster_location"] == i["location"]:
                                startdate = datetime.strptime(j["date"], "%Y-%m-%d")
                                startdate = startdate - timedelta(days = 13) # considering the day in which the location is being declared as Day 1
                            else:
                                return ("No Covid-19 visited location found")                      
        """

        """
        
                            date = datetime.strptime(i["date"],"%Y-%m-%d")
                            delta = today - date
                            if delta.days <= 14:    # if the date is within the last 14 days
                                if i["cluster_location"] == self.data_file[ID][0]["location"]:
                                    infected_list.append(i["cluster_location"]+ " - " + str(delta.days + 1) + " Days ago at " + i["time"])  # add the location and date to the list
                                    return infected_list
        """
        
        """
        for ID, value in self.cluster_file.items():   # loop through all the items in the cluster.json dictionary
            for i in value:
                startdate = datetime.strptime(i["date"], "%Y-%m-%d")
                covid_location.append(i["cluster_location"]),
                covid_location.append(str(startdate - timedelta(days = 13)))  # considering the day in which the location is being declared as Day 1
                covid_location.append(i["date"] + " " + i["time"])

        for ID, value in self.data_file.items():  # loop through all the items in the data.json dictionary
            for i in value:
                if i["nric"] == nric && i["location"] == :
         """


        #today = datetime.strptime(str(datetime.now().date()), "%Y-%m-%d")


    """
        Function to set Covid19 visited location
        Parameters: location, date, time
    """
    def set_covidLocation(self, location, date, time):
        ID = 0 + len(self.cluster_file)
        if ID in self.cluster_file :  # if the ID is already in the dictionary
            ID +=1                     # increment the ID                 
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
                location_list.append(i["cluster_location"] + " - Day "+ str(delta.days + 1))
                
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
                    return ("'"+ location + "' has been removed from the Covid-19 visited location")