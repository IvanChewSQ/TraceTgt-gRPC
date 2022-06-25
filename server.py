from datetime import datetime
from concurrent import futures
from datetime import datetime
import logging
import grpc
import database
import Tracetogether_pb2 as Tracetogether_pb2, Tracetogether_pb2_grpc as Tracetogether_pb2_grpc

class Tracetogether(Tracetogether_pb2_grpc.TracetogetherServicer):
    
    def __init__(self):
        self.db = database.Database()


    """
        Function to checkin:
        (1) Generate checkin time
        (2) Store data into Json file
    """
    def check_in(self, request, context):
        checkin_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db.addDetails(request.name, request.nric, request.location, checkin_time, "")
        return Tracetogether_pb2.CheckIn_Reply(message= "Check-In Successful at " + checkin_time)


    """
        Function to checkout:
        (1) Tally NRIC
        (2) Generate checkout time
        (3) Store data into Json file
    """
    def check_out(self, request, context):
        checkout_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db.updateDetails(request.nric, checkout_time)
        return Tracetogether_pb2.CheckOut_Reply(message= "Check-Out Successful at " + checkout_time)
    

    """
        Function for group checkin:
        (1) Generate checkin time
        (2) Store list data into Json file
    """
    def check_in_grp(self, request, context):
        i = 0        
        checkin_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for nric in request.nric:
            self.db.addDetails(request.name[i], nric, request.location, checkin_time, "")
            i += 1
        return Tracetogether_pb2.CheckIn_Grp_Reply(message= "Group Check-In Successful at " + checkin_time)


    """
        Function for group checkout:
        (1) Tally NRIC
        (2) Generate checkout time
        (3) Store data into Json file
    """
    def check_out_grp(self, request, context):
        checkout_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for nric in request.nric:
            self.db.updateDetails(nric, checkout_time)
        return Tracetogether_pb2.CheckOut_Grp_Reply(message="GroupCheck Out Successful at " + checkout_time)
    

    """
        Function to obtain the history:
        (1) Tally NRIC
        (2) Retrieve data from Json file
    """
    def get_history(self, request, context):
        get_history = self.db.getHistory(request.nric)
        return Tracetogether_pb2.History_Reply(history = get_history)


    """
        Function to declare covid location:
        (1) Set location, date and time 
        (2) Save details into Json file
    """
    def delcare_locations(self, request, context):
        self.db.set_covidLocation(request.location, request.date, request.time)
        return Tracetogether_pb2.Declare_Reply(message = "'"+ request.location + 
            "' declared as Covid-19 visited location on "+ request.date +" at " + request.time + "hrs ")


    """
        Function to view all declared covid locations:
        (1) Retrieve all locations with its number of days being declared from Json file
    """
    def view_locations(self, request, context):
        view_location = self.db.view_covidLocation()
        return Tracetogether_pb2.ViewLocation_Reply(location = view_location)
    

    """
        Function to remove declared covid locations:
        (1) Remove location from Json file
    """
    def remove_locations(self, request, context):
        self.db.remove_covidLocation(request.location)
        return Tracetogether_pb2.RemoveLocation_Reply(message = "'"+ request.location + 
            "' has been removed from the Covid-19 visited location")


def serve():
    listen_addr = '[::]:50051'

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Tracetogether_pb2_grpc.add_TracetogetherServicer_to_server(Tracetogether(), server)

    server.add_insecure_port(listen_addr)
    logging.info('TraceTogether server starting on %s', listen_addr)
    print('TraceTogether server starting on', listen_addr)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
