from asyncio.windows_events import NULL
import json
from datetime import timedelta, datetime

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
            for i in value:
                if i["nric"] == nric:
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
        ID = 0 + len(self.cluster_file) # get last ID
        cluster = {
            ID: [
                {
                    "date": date,
                    "time": time,
                    "location": location
                }
            ]
        }
        self.cluster_file.update(cluster)
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
                location_list.append(i["location"] + " - Day "+str(delta.days))
                
        return location_list


    """
        Function to remove declared Covid-19 Locations
        Arguments: location
    """
    def remove_covidLocation(self, location):
        for ID, value in self.cluster_file.items():    # loop through all the items in the dictionary
            for i in value:
                if i["location"] == location:
                    pass

        json_obj = json.dumps(self.cluster_file, indent=4)
        with open("data/cluster.json", "w") as out:
            out.write(json_obj)

    
    """
        Function to remove declared Covid-19 Locations
        Arguments: location
    """
    def view_affected(self):
        #TODO implement logic
        pass













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