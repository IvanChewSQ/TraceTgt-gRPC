# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from datetime import datetime
from concurrent import futures
from datetime import date, datetime
import logging
import time
import json
import grpc
import test_db
import Tracetogether_pb2 as Tracetogether_pb2, Tracetogether_pb2_grpc as Tracetogether_pb2_grpc

class SafeEntry(Tracetogether_pb2_grpc.TracetogetherServicer):
    
    def __init__(self):
        self.db = test_db.Database()
    
    def Check_In(self, request, context):
        print(request.nric, request.location)
        self.db.addData(request.name, request.nric, request.location, request.checkin)
        return Tracetogether_pb2.Check_In_Reply(message="Check-In Successful")

    def Check_Out(self, request, context):
        print(request.nric, request.checkout)
        self.db.updateData(request.nric, request.checkout)
        return Tracetogether_pb2.Check_Out_Reply(message="Check-Out Successful")

    def Check_In_Group(self, request, context):
        index = 0
        for ic in request.nric:
            self.db.addData(request.name[index], ic, request.location, request.checkin)
            print(request.name[index], ic)
            index += 1
        return Tracetogether_pb2.Grp_Check_In_Reply(message="Group Check-In Successful")

    def Check_Out_Group(self, request, context):
        for ic in request.nric:
            self.db.updateData(ic, request.checkout)
            print(ic)
        return Tracetogether_pb2.Grp_Check_Out_Reply(message=" GroupCheck Out Successful")

    def Location_history(self, request, context):
        locations = self.db.getVisited(request.nric)
        return Tracetogether_pb2.History_Reply(locations=locations)



    def Check_cases(self, request, context):
        return Tracetogether_pb2.Location_Reply(locationList=self.db.getCases(request.nric, self.db.getLocation()))

    def Flag_cases(self, request, context):
        self.db.addCase(request.location, request.datetime)
        return Tracetogether_pb2.Flag_Reply(message="Flagged Case Successful")

    def Flag_location(self, request, context):
        self.db.addLocation(request.location, request.datetime)
        return Tracetogether_pb2.Flag_Reply(message="Flagged Location Successful")

def serve():
    listen_addr = '[::]:50051'

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Tracetogether_pb2_grpc.add_TracetogetherServicer_to_server(SafeEntry(), server)

    server.add_insecure_port(listen_addr)
    logging.info('TraceTogether server starting on %s', listen_addr)
    print('TraceTogether server starting on %s', listen_addr)


    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
