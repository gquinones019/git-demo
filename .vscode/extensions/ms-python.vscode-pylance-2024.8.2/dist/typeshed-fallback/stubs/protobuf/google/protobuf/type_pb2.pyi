"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Protocol Buffers - Google's data interchange format
Copyright 2008 Google Inc.  All rights reserved.
https://developers.google.com/protocol-buffers/

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following disclaimer
in the documentation and/or other materials provided with the
distribution.
    * Neither the name of Google Inc. nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.source_context_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Syntax:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SyntaxEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Syntax.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SYNTAX_PROTO2: _Syntax.ValueType  # 0
    """Syntax `proto2`."""
    SYNTAX_PROTO3: _Syntax.ValueType  # 1
    """Syntax `proto3`."""
    SYNTAX_EDITIONS: _Syntax.ValueType  # 2
    """Syntax `editions`."""

class Syntax(_Syntax, metaclass=_SyntaxEnumTypeWrapper):
    """The syntax in which a protocol buffer element is defined."""

SYNTAX_PROTO2: Syntax.ValueType  # 0
"""Syntax `proto2`."""
SYNTAX_PROTO3: Syntax.ValueType  # 1
"""Syntax `proto3`."""
SYNTAX_EDITIONS: Syntax.ValueType  # 2
"""Syntax `editions`."""
global___Syntax = Syntax

@typing.final
class Type(google.protobuf.message.Message):
    """A protocol buffer message type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    ONEOFS_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    SOURCE_CONTEXT_FIELD_NUMBER: builtins.int
    SYNTAX_FIELD_NUMBER: builtins.int
    EDITION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The fully qualified message name."""
    syntax: global___Syntax.ValueType
    """The source syntax."""
    edition: builtins.str
    """The source edition string, only valid when syntax is SYNTAX_EDITIONS."""
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Field]:
        """The list of fields."""

    @property
    def oneofs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The list of types appearing in `oneof` definitions in this type."""

    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Option]:
        """The protocol buffer options."""

    @property
    def source_context(self) -> google.protobuf.source_context_pb2.SourceContext:
        """The source context."""

    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        fields: collections.abc.Iterable[global___Field] | None = ...,
        oneofs: collections.abc.Iterable[builtins.str] | None = ...,
        options: collections.abc.Iterable[global___Option] | None = ...,
        source_context: google.protobuf.source_context_pb2.SourceContext | None = ...,
        syntax: global___Syntax.ValueType | None = ...,
        edition: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["source_context", b"source_context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["edition", b"edition", "fields", b"fields", "name", b"name", "oneofs", b"oneofs", "options", b"options", "source_context", b"source_context", "syntax", b"syntax"]) -> None: ...

global___Type = Type

@typing.final
class Field(google.protobuf.message.Message):
    """A single field of a message type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Kind:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _KindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Field._Kind.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNKNOWN: Field._Kind.ValueType  # 0
        """Field type unknown."""
        TYPE_DOUBLE: Field._Kind.ValueType  # 1
        """Field type double."""
        TYPE_FLOAT: Field._Kind.ValueType  # 2
        """Field type float."""
        TYPE_INT64: Field._Kind.ValueType  # 3
        """Field type int64."""
        TYPE_UINT64: Field._Kind.ValueType  # 4
        """Field type uint64."""
        TYPE_INT32: Field._Kind.ValueType  # 5
        """Field type int32."""
        TYPE_FIXED64: Field._Kind.ValueType  # 6
        """Field type fixed64."""
        TYPE_FIXED32: Field._Kind.ValueType  # 7
        """Field type fixed32."""
        TYPE_BOOL: Field._Kind.ValueType  # 8
        """Field type bool."""
        TYPE_STRING: Field._Kind.ValueType  # 9
        """Field type string."""
        TYPE_GROUP: Field._Kind.ValueType  # 10
        """Field type group. Proto2 syntax only, and deprecated."""
        TYPE_MESSAGE: Field._Kind.ValueType  # 11
        """Field type message."""
        TYPE_BYTES: Field._Kind.ValueType  # 12
        """Field type bytes."""
        TYPE_UINT32: Field._Kind.ValueType  # 13
        """Field type uint32."""
        TYPE_ENUM: Field._Kind.ValueType  # 14
        """Field type enum."""
        TYPE_SFIXED32: Field._Kind.ValueType  # 15
        """Field type sfixed32."""
        TYPE_SFIXED64: Field._Kind.ValueType  # 16
        """Field type sfixed64."""
        TYPE_SINT32: Field._Kind.ValueType  # 17
        """Field type sint32."""
        TYPE_SINT64: Field._Kind.ValueType  # 18
        """Field type sint64."""

    class Kind(_Kind, metaclass=_KindEnumTypeWrapper):
        """Basic field types."""

    TYPE_UNKNOWN: Field.Kind.ValueType  # 0
    """Field type unknown."""
    TYPE_DOUBLE: Field.Kind.ValueType  # 1
    """Field type double."""
    TYPE_FLOAT: Field.Kind.ValueType  # 2
    """Field type float."""
    TYPE_INT64: Field.Kind.ValueType  # 3
    """Field type int64."""
    TYPE_UINT64: Field.Kind.ValueType  # 4
    """Field type uint64."""
    TYPE_INT32: Field.Kind.ValueType  # 5
    """Field type int32."""
    TYPE_FIXED64: Field.Kind.ValueType  # 6
    """Field type fixed64."""
    TYPE_FIXED32: Field.Kind.ValueType  # 7
    """Field type fixed32."""
    TYPE_BOOL: Field.Kind.ValueType  # 8
    """Field type bool."""
    TYPE_STRING: Field.Kind.ValueType  # 9
    """Field type string."""
    TYPE_GROUP: Field.Kind.ValueType  # 10
    """Field type group. Proto2 syntax only, and deprecated."""
    TYPE_MESSAGE: Field.Kind.ValueType  # 11
    """Field type message."""
    TYPE_BYTES: Field.Kind.ValueType  # 12
    """Field type bytes."""
    TYPE_UINT32: Field.Kind.ValueType  # 13
    """Field type uint32."""
    TYPE_ENUM: Field.Kind.ValueType  # 14
    """Field type enum."""
    TYPE_SFIXED32: Field.Kind.ValueType  # 15
    """Field type sfixed32."""
    TYPE_SFIXED64: Field.Kind.ValueType  # 16
    """Field type sfixed64."""
    TYPE_SINT32: Field.Kind.ValueType  # 17
    """Field type sint32."""
    TYPE_SINT64: Field.Kind.ValueType  # 18
    """Field type sint64."""

    class _Cardinality:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CardinalityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Field._Cardinality.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CARDINALITY_UNKNOWN: Field._Cardinality.ValueType  # 0
        """For fields with unknown cardinality."""
        CARDINALITY_OPTIONAL: Field._Cardinality.ValueType  # 1
        """For optional fields."""
        CARDINALITY_REQUIRED: Field._Cardinality.ValueType  # 2
        """For required fields. Proto2 syntax only."""
        CARDINALITY_REPEATED: Field._Cardinality.ValueType  # 3
        """For repeated fields."""

    class Cardinality(_Cardinality, metaclass=_CardinalityEnumTypeWrapper):
        """Whether a field is optional, required, or repeated."""

    CARDINALITY_UNKNOWN: Field.Cardinality.ValueType  # 0
    """For fields with unknown cardinality."""
    CARDINALITY_OPTIONAL: Field.Cardinality.ValueType  # 1
    """For optional fields."""
    CARDINALITY_REQUIRED: Field.Cardinality.ValueType  # 2
    """For required fields. Proto2 syntax only."""
    CARDINALITY_REPEATED: Field.Cardinality.ValueType  # 3
    """For repeated fields."""

    KIND_FIELD_NUMBER: builtins.int
    CARDINALITY_FIELD_NUMBER: builtins.int
    NUMBER_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TYPE_URL_FIELD_NUMBER: builtins.int
    ONEOF_INDEX_FIELD_NUMBER: builtins.int
    PACKED_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    JSON_NAME_FIELD_NUMBER: builtins.int
    DEFAULT_VALUE_FIELD_NUMBER: builtins.int
    kind: global___Field.Kind.ValueType
    """The field type."""
    cardinality: global___Field.Cardinality.ValueType
    """The field cardinality."""
    number: builtins.int
    """The field number."""
    name: builtins.str
    """The field name."""
    type_url: builtins.str
    """The field type URL, without the scheme, for message or enumeration
    types. Example: `"type.googleapis.com/google.protobuf.Timestamp"`.
    """
    oneof_index: builtins.int
    """The index of the field type in `Type.oneofs`, for message or enumeration
    types. The first type has index 1; zero means the type is not in the list.
    """
    packed: builtins.bool
    """Whether to use alternative packed wire representation."""
    json_name: builtins.str
    """The field JSON name."""
    default_value: builtins.str
    """The string value of the default value of this field. Proto2 syntax only."""
    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Option]:
        """The protocol buffer options."""

    def __init__(
        self,
        *,
        kind: global___Field.Kind.ValueType | None = ...,
        cardinality: global___Field.Cardinality.ValueType | None = ...,
        number: builtins.int | None = ...,
        name: builtins.str | None = ...,
        type_url: builtins.str | None = ...,
        oneof_index: builtins.int | None = ...,
        packed: builtins.bool | None = ...,
        options: collections.abc.Iterable[global___Option] | None = ...,
        json_name: builtins.str | None = ...,
        default_value: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cardinality", b"cardinality", "default_value", b"default_value", "json_name", b"json_name", "kind", b"kind", "name", b"name", "number", b"number", "oneof_index", b"oneof_index", "options", b"options", "packed", b"packed", "type_url", b"type_url"]) -> None: ...

global___Field = Field

@typing.final
class Enum(google.protobuf.message.Message):
    """Enum type definition."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ENUMVALUE_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    SOURCE_CONTEXT_FIELD_NUMBER: builtins.int
    SYNTAX_FIELD_NUMBER: builtins.int
    EDITION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Enum type name."""
    syntax: global___Syntax.ValueType
    """The source syntax."""
    edition: builtins.str
    """The source edition string, only valid when syntax is SYNTAX_EDITIONS."""
    @property
    def enumvalue(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EnumValue]:
        """Enum value definitions."""

    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Option]:
        """Protocol buffer options."""

    @property
    def source_context(self) -> google.protobuf.source_context_pb2.SourceContext:
        """The source context."""

    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        enumvalue: collections.abc.Iterable[global___EnumValue] | None = ...,
        options: collections.abc.Iterable[global___Option] | None = ...,
        source_context: google.protobuf.source_context_pb2.SourceContext | None = ...,
        syntax: global___Syntax.ValueType | None = ...,
        edition: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["source_context", b"source_context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["edition", b"edition", "enumvalue", b"enumvalue", "name", b"name", "options", b"options", "source_context", b"source_context", "syntax", b"syntax"]) -> None: ...

global___Enum = Enum

@typing.final
class EnumValue(google.protobuf.message.Message):
    """Enum value definition."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    NUMBER_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Enum value name."""
    number: builtins.int
    """Enum value number."""
    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Option]:
        """Protocol buffer options."""

    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        number: builtins.int | None = ...,
        options: collections.abc.Iterable[global___Option] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "number", b"number", "options", b"options"]) -> None: ...

global___EnumValue = EnumValue

@typing.final
class Option(google.protobuf.message.Message):
    """A protocol buffer option, which can be attached to a message, field,
    enumeration, etc.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The option's name. For protobuf built-in options (options defined in
    descriptor.proto), this is the short name. For example, `"map_entry"`.
    For custom options, it should be the fully-qualified name. For example,
    `"google.api.http"`.
    """
    @property
    def value(self) -> google.protobuf.any_pb2.Any:
        """The option's value packed in an Any message. If the value is a primitive,
        the corresponding wrapper type defined in google/protobuf/wrappers.proto
        should be used. If the value is an enum, it should be stored as an int32
        value using the google.protobuf.Int32Value type.
        """

    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        value: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "value", b"value"]) -> None: ...

global___Option = Option
