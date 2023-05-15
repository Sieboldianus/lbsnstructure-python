# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lbsnstructure/spatial.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from lbsnstructure import social_pb2 as lbsnstructure_dot_social__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1blbsnstructure/spatial.proto\x12\x0elbsn.structure\x1a\x1albsnstructure/social.proto\"\xf0\x03\n\x05Place\x12*\n\x04pkey\x18\x01 \x01(\x0b\x32\x1c.lbsn.structure.CompositeKey\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11name_alternatives\x18\x03 \x03(\t\x12\x12\n\npost_count\x18\x04 \x01(\x03\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x13\n\x0bgeom_center\x18\x06 \x01(\t\x12\x11\n\tgeom_area\x18\x07 \x01(\t\x12/\n\tcity_pkey\x18\x08 \x01(\x0b\x32\x1c.lbsn.structure.CompositeKey\x12\x19\n\x11place_description\x18\t \x01(\t\x12\x15\n\rplace_website\x18\n \x01(\t\x12\x13\n\x0bplace_phone\x18\x0b \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x0c \x01(\t\x12\x10\n\x08zip_code\x18\r \x01(\t\x12\x15\n\rcheckin_count\x18\x0e \x01(\x03\x12\x12\n\nlike_count\x18\x0f \x01(\x03\x12\x15\n\rparent_places\x18\x10 \x03(\t\x12\x39\n\nattributes\x18\x11 \x03(\x0b\x32%.lbsn.structure.Place.AttributesEntry\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd6\x01\n\x04\x43ity\x12*\n\x04pkey\x18\x01 \x01(\x0b\x32\x1c.lbsn.structure.CompositeKey\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11name_alternatives\x18\x03 \x03(\t\x12\x10\n\x08sub_type\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x13\n\x0bgeom_center\x18\x06 \x01(\t\x12\x11\n\tgeom_area\x18\x07 \x01(\t\x12\x32\n\x0c\x63ountry_pkey\x18\x08 \x01(\x0b\x32\x1c.lbsn.structure.CompositeKey\"\x93\x01\n\x07\x43ountry\x12*\n\x04pkey\x18\x01 \x01(\x0b\x32\x1c.lbsn.structure.CompositeKey\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11name_alternatives\x18\x03 \x03(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x13\n\x0bgeom_center\x18\x05 \x01(\t\x12\x11\n\tgeom_area\x18\x06 \x01(\tb\x06proto3')



_PLACE = DESCRIPTOR.message_types_by_name['Place']
_PLACE_ATTRIBUTESENTRY = _PLACE.nested_types_by_name['AttributesEntry']
_CITY = DESCRIPTOR.message_types_by_name['City']
_COUNTRY = DESCRIPTOR.message_types_by_name['Country']
Place = _reflection.GeneratedProtocolMessageType('Place', (_message.Message,), {

  'AttributesEntry' : _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLACE_ATTRIBUTESENTRY,
    '__module__' : 'lbsnstructure.spatial_pb2'
    # @@protoc_insertion_point(class_scope:lbsn.structure.Place.AttributesEntry)
    })
  ,
  'DESCRIPTOR' : _PLACE,
  '__module__' : 'lbsnstructure.spatial_pb2'
  # @@protoc_insertion_point(class_scope:lbsn.structure.Place)
  })
_sym_db.RegisterMessage(Place)
_sym_db.RegisterMessage(Place.AttributesEntry)

City = _reflection.GeneratedProtocolMessageType('City', (_message.Message,), {
  'DESCRIPTOR' : _CITY,
  '__module__' : 'lbsnstructure.spatial_pb2'
  # @@protoc_insertion_point(class_scope:lbsn.structure.City)
  })
_sym_db.RegisterMessage(City)

Country = _reflection.GeneratedProtocolMessageType('Country', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRY,
  '__module__' : 'lbsnstructure.spatial_pb2'
  # @@protoc_insertion_point(class_scope:lbsn.structure.Country)
  })
_sym_db.RegisterMessage(Country)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLACE_ATTRIBUTESENTRY._options = None
  _PLACE_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _PLACE._serialized_start=76
  _PLACE._serialized_end=572
  _PLACE_ATTRIBUTESENTRY._serialized_start=523
  _PLACE_ATTRIBUTESENTRY._serialized_end=572
  _CITY._serialized_start=575
  _CITY._serialized_end=789
  _COUNTRY._serialized_start=792
  _COUNTRY._serialized_end=939
# @@protoc_insertion_point(module_scope)