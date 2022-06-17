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
import Tracetogether_pb2, Tracetogether_pb2_grpc

class UserInfoService(Tracetogether_pb2_grpc.UserInfoServicer):
    def Username(self, request, context):
        response = Tracetogether_pb2.UserRequest()
        response.name = users_method.users_info(request.user_id,request.name,request.password)
        return response



server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
Tracetogether_pb2_grpc.add_UserInfoServicer_to_server(
        UserInfoService(), server)
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
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
        return Tracetogether_pb2.details(message='%s, Completed!' % request.status)
    except: 
      return Tracetogether_pb2.details(message='%s, Unsuccessful! Please try again...' % request.status)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    (Checkin(), server)
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
