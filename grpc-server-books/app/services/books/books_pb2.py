# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: books.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x62ooks.proto\x12\x05\x62ooks\"Z\n\x05\x42ooks\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x11\n\tpublisher\x18\x05 \x01(\t\"\x1e\n\x10\x42ooksRequestById\x12\n\n\x02id\x18\x01 \x01(\x05\x32\x46\n\x0c\x42ooksRequest\x12\x36\n\x0bGetBookById\x12\x17.books.BooksRequestById\x1a\x0c.books.Books\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'books_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOKS._serialized_start=22
  _BOOKS._serialized_end=112
  _BOOKSREQUESTBYID._serialized_start=114
  _BOOKSREQUESTBYID._serialized_end=144
  _BOOKSREQUEST._serialized_start=146
  _BOOKSREQUEST._serialized_end=216
# @@protoc_insertion_point(module_scope)
