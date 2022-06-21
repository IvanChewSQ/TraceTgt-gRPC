from asyncio.windows_events import NULL
import json
from datetime import timedelta, datetime

class Database():
    
    def __init__(self):
        self.data_file = json.load(open("data/data.json", "r"))
        self.cluster_file = json.load(open("data/cluster.json", "r"))


    """
        Function to add users details into json file
        Arguments: name, nric, location, checkin time, checkout time
    """
    def addDetails(self, name, nric, location, checkin_time, checkout_time):
        data = {
            nric: [
                {
                    "nric": nric,
                    "name": name,
                    "location": location,
                    "checkInDateTime": checkin_time,
                    "checkOutDateTime": checkout_time
                }
            ]
        }
        self.data_file.update(data)
        json_obj = json.dumps(self.data_file, indent=4)
        with open("data/data.json", "w") as out:
            out.write(json_obj)


    """
        Function to update users checkout time in json file
        Arguments: nric, checkout time
    """
    def updateDetails(self, nric, checkout_time):
        user = self.data_file[nric]
        user[0]["checkOutDateTime"] = checkout_time
        json_obj = json.dumps(self.data_file, indent=4)
        with open("data/data.json", "w") as out:
            out.write(json_obj)

    
    """
        Function to update users checkout time in json file
        Arguments: nric, checkout time
    """
    def getHistory(self, nric, checkout_time):
        #TODO get the list of History based on input NRIC
        pass


    """
        Function to update users checkout time in json file
        Arguments: nric, checkout time
    """
    def covidLocation(self, location, date, time):
        cluster = {
            location: [
                {
                    "Date": date,
                    "Time": time
                }
            ]
        }
        self.cluster_file.update(cluster)
        json_obj = json.dumps(self.cluster_file, indent=4)
        with open("data/cluster.json", "w") as out:
            out.write(json_obj)









    '''Function to get list of locations visited by a Covid case within past 14 days
    Returns list of locations'''
    def getLocation(self):
        locationList = []
        
        ## 2022/6/4
        now = datetime.now()
        cur = now - timedelta(days=14)

        for i in self.cluster_file:
            locationDate = self.cluster_file[i]["Date"]
            locationDate = datetime.strptime(locationDate, '%d/%m/%Y')

            if (locationDate > cur):
                locationList.append(i)

        print(locationList)

        return locationList
    
    '''Function to get list of locations visited by user
    Returns list of locations'''
    def getVisited(self, nric):
        locationList = []
        
        ## 2022/6/4
        now = datetime.now()
        cur = now - timedelta(days=14)
        
        for i in self.data_file[nric]:
            locationList.append(i["location"])

        print(locationList)

        return locationList

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

    '''Reusable function to check if NRIC exists in data.json
    Returns true if so'''
    def nricExists(self, nric):
        return False