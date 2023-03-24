# StructuralAnalysisFormat-Protobuf

A protobuf for www.saf.guide

## About SAF

<www.saf.guide>


## python_protobuf

run generate_proto.py to generate proto files form example proto file

than you see the  saf.proto generated in the proto folder

## python_betterproto

install the protobuf from  [google protobuf](https://protobuf.dev/downloads/)

using protoc with betterproto to generate python code
<https://github.com/danielgtaylor/python-betterproto>

` pip install betterproto `

` protoc  -I . --python_betterproto_out=src proto\saf.proto `