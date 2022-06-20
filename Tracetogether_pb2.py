# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Tracetogether.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13Tracetogether.proto\"?\n\x0f\x43heckIn_Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04nric\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\" \n\rCheckIn_Reply\x12\x0f\n\x07message\x18\x01 \x01(\t\" \n\x10\x43heckOut_Request\x12\x0c\n\x04nric\x18\x01 \x01(\t\"!\n\x0e\x43heckOut_Reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"C\n\x13\x43heckIn_Grp_Request\x12\x0c\n\x04name\x18\x01 \x03(\t\x12\x0c\n\x04nric\x18\x02 \x03(\t\x12\x10\n\x08location\x18\x03 \x01(\t\"$\n\x11\x43heckIn_Grp_Reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"$\n\x14\x43heckOut_Grp_Request\x12\x0c\n\x04nric\x18\x01 \x03(\t\"%\n\x12\x43heckOut_Grp_Reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0fHistory_Request\x12\x0c\n\x04nric\x18\x01 \x01(\t\"\"\n\rHistory_Reply\x12\x11\n\tlocations\x18\x01 \x03(\t\"2\n\x0c\x46lag_Request\x12\x10\n\x08location\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x02 \x01(\t\"\x1d\n\nFlag_Reply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xcc\x02\n\rTracetogether\x12.\n\x08\x63heck_in\x12\x10.CheckIn_Request\x1a\x0e.CheckIn_Reply\"\x00\x12\x31\n\tcheck_out\x12\x11.CheckOut_Request\x1a\x0f.CheckOut_Reply\"\x00\x12:\n\x0c\x63heck_in_grp\x12\x14.CheckIn_Grp_Request\x1a\x12.CheckIn_Grp_Reply\"\x00\x12=\n\rcheck_out_grp\x12\x15.CheckOut_Grp_Request\x1a\x13.CheckOut_Grp_Reply\"\x00\x12\x31\n\x0bget_history\x12\x10.History_Request\x1a\x0e.History_Reply\"\x00\x12*\n\nflag_cases\x12\r.Flag_Request\x1a\x0b.Flag_Reply\"\x00\x62\x06proto3')



_CHECKIN_REQUEST = DESCRIPTOR.message_types_by_name['CheckIn_Request']
_CHECKIN_REPLY = DESCRIPTOR.message_types_by_name['CheckIn_Reply']
_CHECKOUT_REQUEST = DESCRIPTOR.message_types_by_name['CheckOut_Request']
_CHECKOUT_REPLY = DESCRIPTOR.message_types_by_name['CheckOut_Reply']
_CHECKIN_GRP_REQUEST = DESCRIPTOR.message_types_by_name['CheckIn_Grp_Request']
_CHECKIN_GRP_REPLY = DESCRIPTOR.message_types_by_name['CheckIn_Grp_Reply']
_CHECKOUT_GRP_REQUEST = DESCRIPTOR.message_types_by_name['CheckOut_Grp_Request']
_CHECKOUT_GRP_REPLY = DESCRIPTOR.message_types_by_name['CheckOut_Grp_Reply']
_HISTORY_REQUEST = DESCRIPTOR.message_types_by_name['History_Request']
_HISTORY_REPLY = DESCRIPTOR.message_types_by_name['History_Reply']
_FLAG_REQUEST = DESCRIPTOR.message_types_by_name['Flag_Request']
_FLAG_REPLY = DESCRIPTOR.message_types_by_name['Flag_Reply']
CheckIn_Request = _reflection.GeneratedProtocolMessageType('CheckIn_Request', (_message.Message,), {
  'DESCRIPTOR' : _CHECKIN_REQUEST,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:CheckIn_Request)
  })
_sym_db.RegisterMessage(CheckIn_Request)

CheckIn_Reply = _reflection.GeneratedProtocolMessageType('CheckIn_Reply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKIN_REPLY,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:CheckIn_Reply)
  })
_sym_db.RegisterMessage(CheckIn_Reply)

CheckOut_Request = _reflection.GeneratedProtocolMessageType('CheckOut_Request', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUT_REQUEST,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:CheckOut_Request)
  })
_sym_db.RegisterMessage(CheckOut_Request)

CheckOut_Reply = _reflection.GeneratedProtocolMessageType('CheckOut_Reply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUT_REPLY,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:CheckOut_Reply)
  })
_sym_db.RegisterMessage(CheckOut_Reply)

CheckIn_Grp_Request = _reflection.GeneratedProtocolMessageType('CheckIn_Grp_Request', (_message.Message,), {
  'DESCRIPTOR' : _CHECKIN_GRP_REQUEST,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:CheckIn_Grp_Request)
  })
_sym_db.RegisterMessage(CheckIn_Grp_Request)

CheckIn_Grp_Reply = _reflection.GeneratedProtocolMessageType('CheckIn_Grp_Reply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKIN_GRP_REPLY,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:CheckIn_Grp_Reply)
  })
_sym_db.RegisterMessage(CheckIn_Grp_Reply)

CheckOut_Grp_Request = _reflection.GeneratedProtocolMessageType('CheckOut_Grp_Request', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUT_GRP_REQUEST,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:CheckOut_Grp_Request)
  })
_sym_db.RegisterMessage(CheckOut_Grp_Request)

CheckOut_Grp_Reply = _reflection.GeneratedProtocolMessageType('CheckOut_Grp_Reply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKOUT_GRP_REPLY,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:CheckOut_Grp_Reply)
  })
_sym_db.RegisterMessage(CheckOut_Grp_Reply)

History_Request = _reflection.GeneratedProtocolMessageType('History_Request', (_message.Message,), {
  'DESCRIPTOR' : _HISTORY_REQUEST,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:History_Request)
  })
_sym_db.RegisterMessage(History_Request)

History_Reply = _reflection.GeneratedProtocolMessageType('History_Reply', (_message.Message,), {
  'DESCRIPTOR' : _HISTORY_REPLY,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:History_Reply)
  })
_sym_db.RegisterMessage(History_Reply)

Flag_Request = _reflection.GeneratedProtocolMessageType('Flag_Request', (_message.Message,), {
  'DESCRIPTOR' : _FLAG_REQUEST,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:Flag_Request)
  })
_sym_db.RegisterMessage(Flag_Request)

Flag_Reply = _reflection.GeneratedProtocolMessageType('Flag_Reply', (_message.Message,), {
  'DESCRIPTOR' : _FLAG_REPLY,
  '__module__' : 'Tracetogether_pb2'
  # @@protoc_insertion_point(class_scope:Flag_Reply)
  })
_sym_db.RegisterMessage(Flag_Reply)

_TRACETOGETHER = DESCRIPTOR.services_by_name['Tracetogether']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHECKIN_REQUEST._serialized_start=23
  _CHECKIN_REQUEST._serialized_end=86
  _CHECKIN_REPLY._serialized_start=88
  _CHECKIN_REPLY._serialized_end=120
  _CHECKOUT_REQUEST._serialized_start=122
  _CHECKOUT_REQUEST._serialized_end=154
  _CHECKOUT_REPLY._serialized_start=156
  _CHECKOUT_REPLY._serialized_end=189
  _CHECKIN_GRP_REQUEST._serialized_start=191
  _CHECKIN_GRP_REQUEST._serialized_end=258
  _CHECKIN_GRP_REPLY._serialized_start=260
  _CHECKIN_GRP_REPLY._serialized_end=296
  _CHECKOUT_GRP_REQUEST._serialized_start=298
  _CHECKOUT_GRP_REQUEST._serialized_end=334
  _CHECKOUT_GRP_REPLY._serialized_start=336
  _CHECKOUT_GRP_REPLY._serialized_end=373
  _HISTORY_REQUEST._serialized_start=375
  _HISTORY_REQUEST._serialized_end=406
  _HISTORY_REPLY._serialized_start=408
  _HISTORY_REPLY._serialized_end=442
  _FLAG_REQUEST._serialized_start=444
  _FLAG_REQUEST._serialized_end=494
  _FLAG_REPLY._serialized_start=496
  _FLAG_REPLY._serialized_end=525
  _TRACETOGETHER._serialized_start=528
  _TRACETOGETHER._serialized_end=860
# @@protoc_insertion_point(module_scope)