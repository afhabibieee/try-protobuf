# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bookstore.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x62ookstore.proto\x12\tbookstore\"N\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0c\n\x04isbn\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\x01\"\x1c\n\x0eGetBookRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1f\n\x11\x44\x65leteBookRequest\x12\n\n\x02id\x18\x01 \x01(\t\"1\n\x12\x44\x65leteBookResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x07\n\x05\x45mpty\"3\n\x11ListBooksResponse\x12\x1e\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x0f.bookstore.Book2\xf9\x01\n\x0b\x42ookService\x12+\n\x07\x41\x64\x64\x42ook\x12\x0f.bookstore.Book\x1a\x0f.bookstore.Book\x12\x35\n\x07GetBook\x12\x19.bookstore.GetBookRequest\x1a\x0f.bookstore.Book\x12I\n\nDeleteBook\x12\x1c.bookstore.DeleteBookRequest\x1a\x1d.bookstore.DeleteBookResponse\x12;\n\tListBooks\x12\x10.bookstore.Empty\x1a\x1c.bookstore.ListBooksResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bookstore_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BOOK']._serialized_start=30
  _globals['_BOOK']._serialized_end=108
  _globals['_GETBOOKREQUEST']._serialized_start=110
  _globals['_GETBOOKREQUEST']._serialized_end=138
  _globals['_DELETEBOOKREQUEST']._serialized_start=140
  _globals['_DELETEBOOKREQUEST']._serialized_end=171
  _globals['_DELETEBOOKRESPONSE']._serialized_start=173
  _globals['_DELETEBOOKRESPONSE']._serialized_end=222
  _globals['_EMPTY']._serialized_start=224
  _globals['_EMPTY']._serialized_end=231
  _globals['_LISTBOOKSRESPONSE']._serialized_start=233
  _globals['_LISTBOOKSRESPONSE']._serialized_end=284
  _globals['_BOOKSERVICE']._serialized_start=287
  _globals['_BOOKSERVICE']._serialized_end=536
# @@protoc_insertion_point(module_scope)
