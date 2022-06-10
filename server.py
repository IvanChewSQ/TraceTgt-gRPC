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

from concurrent import futures
from datetime import date, datetime
import logging
import json
import grpc
import Tracetogether_pb2, Tracetogether_pb2_grpc

class Greeter(Tracetogether_pb2_grpc.GreeterServicer):

  def SayHello(self, request, context):
    return Tracetogether_pb2.HelloReply(message='Connected!, %s!' % request.name)

class Checkin(Tracetogether_pb2_grpc.CheckinServicer):

  def details(self, request, context):
    data = {
        "Name": request.name,
        "NRIC": request.nric,
        "Location": request.location,
        "Status": request.status,
        "Date": date.today().strftime("%B %d, %Y"),
        "Time": datetime.now().strftime("%H:%M:%S")
    }

    try:
      with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
    except: 
      return Tracetogether_pb2.details(message='%s, Unsuccessful! Please try again...' % request.status)
    return Tracetogether_pb2.details(message='%s, Completed!' % request.status)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    (Greeter(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info('TraceTogether server starting on %s', listen_addr)
    print('TraceTogether server starting on %s', listen_addr)

    Tracetogether_pb2_grpc.add_CheckinServicer_to_server(Checkin(),server)
    
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
