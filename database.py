from asyncio.windows_events import NULL
import json
from datetime import timedelta, datetime

class Database():
    
    '''Read and open json file first for optimised performance'''
    def __init__(self):
        self.data_file = json.load(open("data/data.json", "r"))
        self.location_file = json.load(open("data/cluster.json", "r"))

    '''Function to add new SafeEntry data into datas.json
    Args: user's name, nric, visiting location and check in datetime'''
    def addDetails(self, name, nric, location, checkin_time, checkout_time):
        ID=0 + len(self.data_file)
        datas = {
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

        self.data_file.update(datas)
        json_obj = json.dumps(self.data_file, indent=4)
        with open("data/data.json", "w") as out:
            out.write(json_obj)

    '''Function to update existing SafeEntry entry with check out datetime
    Args: user's nric and check out datetime'''
    def updateDetails(self, nric, dateTime):

        ID=0 + len(self.data_file)-1 # get last ID
        for ID, value in self.data_file.items():    # loop through all the items in the dictionary
            for i in value:
                if i["nric"] == nric:
                    i["checkOutDateTime"] = dateTime

        json_obj = json.dumps(self.data_file, indent=4)
        with open("data/data.json", "w") as out:
            out.write(json_obj)

    def addLocation(self, location, dateTime):
        location = {
            location: 
            {
                "Date": date,
                "Time": time
            }
        }

        self.location_file.update(location)

        json_obj = json.dumps(self.location_file, indent=4)

        with open("data/clusters.json", "w") as out:
            out.write(json_obj)

    '''Function to get list of locations visited by a Covid case within past 14 days
    Returns list of locations'''
    def getLocation(self):
        locationList = []
        
        ## 2022/6/4
        now = datetime.now()
        cur = now - timedelta(days=14)

        for i in self.location_file:
            locationDate = self.location_file[i]["Date"]
            locationDate = datetime.strptime(locationDate, '%d/%m/%Y')

            if (locationDate > cur):
                locationList.append(i)

        print(locationList)

        return locationList
    
    '''Function to get list of locations visited by user
    Returns list of locations'''
    def getHistory(self, nric):
        history_list = []    # list of dictionaries

        for ID, value in self.data_file.items():   # loop through all the items in the dictionary
            for i in value:
                if i["nric"] == nric:
                    history_list.append(i["location"])
                    history_list.append(i["checkInDateTime"])
                    history_list.append(i["checkOutDateTime"])
         
        history = [history_list[i:i + 3] for i in range(0, len(history_list), 3)]
        return history

    def getLocationHistory(self, location):

        locationHistory = []

        for ID, value in self.data_file.items():
            for i in value:
                if i["location"] == location:
                    locationHistory.append(i)

        return locationHistory



        
        ## 2022/6/4
        #now = datetime.now()


    '''Function to check if user has visited an infected location within past 14 days
    Args: nric of user and list of infected locations
    Returns TODO'''
    def getCases(self, nric, infectedLocation: list):
        LocationList = []

        now = datetime.now()
        cur = now - timedelta(days=14)
      
        visitedLocation = self.data_file[nric]
        # print(visitedLocation)
        for j in visitedLocation:
            locations = j["location"]
            locationDateTime = j["checkInDateTime"]
            locationDateTime = datetime.strptime(locationDateTime, '%d/%m/%Y, %H:%M:%S')

            if locationDateTime > cur and locations in infectedLocation:
                locationDateTime = datetime.strftime(locationDateTime, '%d/%m/%Y, %H:%M:%S')
                LocationList.append(locations)
                LocationList.append(locationDateTime)

        print(LocationList)
        return LocationList

    '''Reusable function to check if NRIC exists in entry.json
    Returns true if so'''
    def nricExists(self, nric):
        return False