# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/puzzle_input.proto
# Protobuf Python Version: 5.29.0-rc1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '-rc1',
    'proto/puzzle_input.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/puzzle_input.proto\"\xc2\x01\n\x0bPuzzleInput\x12$\n\x07puzzles\x18\x01 \x03(\x0b\x32\x13.PuzzleInput.Puzzle\x1a\x8c\x01\n\x06Puzzle\x12\x11\n\tpuzzle_id\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12%\n\x04rows\x18\x04 \x03(\x0b\x32\x17.PuzzleInput.Puzzle.Row\x1a)\n\x03Row\x12\x0f\n\x07symbols\x18\x01 \x03(\t\x12\x11\n\tend_value\x18\x02 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.puzzle_input_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PUZZLEINPUT']._serialized_start=29
  _globals['_PUZZLEINPUT']._serialized_end=223
  _globals['_PUZZLEINPUT_PUZZLE']._serialized_start=83
  _globals['_PUZZLEINPUT_PUZZLE']._serialized_end=223
  _globals['_PUZZLEINPUT_PUZZLE_ROW']._serialized_start=182
  _globals['_PUZZLEINPUT_PUZZLE_ROW']._serialized_end=223
# @@protoc_insertion_point(module_scope)
