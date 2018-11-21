# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/wca-state-machine.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/wca-state-machine.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dproto/wca-state-machine.proto\".\n\x10TriggerPredicate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"\'\n\tProcessor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"\x80\x01\n\nTransition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x12trigger_predicates\x18\x02 \x03(\x0b\x32\x11.TriggerPredicate\x12!\n\x0binstruction\x18\x03 \x01(\x0b\x32\x0c.Instruction\x12\x12\n\nnext_state\x18\x04 \x01(\t\":\n\x0bInstruction\x12\r\n\x05\x61udio\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\x0c\x12\r\n\x05video\x18\x03 \x01(\x0c\"W\n\x05State\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\nprocessors\x18\x04 \x03(\x0b\x32\n.Processor\x12 \n\x0btransitions\x18\x02 \x03(\x0b\x32\x0b.Transition\"\x8e\x01\n\x0cStateMachine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x06states\x18\x02 \x03(\x0b\x32\x06.State\x12)\n\x06\x61ssets\x18\x03 \x03(\x0b\x32\x19.StateMachine.AssetsEntry\x1a-\n\x0b\x41ssetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x62\x06proto3')
)




_TRIGGERPREDICATE = _descriptor.Descriptor(
  name='TriggerPredicate',
  full_name='TriggerPredicate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='TriggerPredicate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='TriggerPredicate.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=79,
)


_PROCESSOR = _descriptor.Descriptor(
  name='Processor',
  full_name='Processor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Processor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Processor.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=120,
)


_TRANSITION = _descriptor.Descriptor(
  name='Transition',
  full_name='Transition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Transition.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger_predicates', full_name='Transition.trigger_predicates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instruction', full_name='Transition.instruction', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_state', full_name='Transition.next_state', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=251,
)


_INSTRUCTION = _descriptor.Descriptor(
  name='Instruction',
  full_name='Instruction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='Instruction.audio', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='Instruction.image', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video', full_name='Instruction.video', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=311,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='State.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processors', full_name='State.processors', index=1,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transitions', full_name='State.transitions', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=400,
)


_STATEMACHINE_ASSETSENTRY = _descriptor.Descriptor(
  name='AssetsEntry',
  full_name='StateMachine.AssetsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='StateMachine.AssetsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='StateMachine.AssetsEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=545,
)

_STATEMACHINE = _descriptor.Descriptor(
  name='StateMachine',
  full_name='StateMachine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='StateMachine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='states', full_name='StateMachine.states', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assets', full_name='StateMachine.assets', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATEMACHINE_ASSETSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=545,
)

_TRANSITION.fields_by_name['trigger_predicates'].message_type = _TRIGGERPREDICATE
_TRANSITION.fields_by_name['instruction'].message_type = _INSTRUCTION
_STATE.fields_by_name['processors'].message_type = _PROCESSOR
_STATE.fields_by_name['transitions'].message_type = _TRANSITION
_STATEMACHINE_ASSETSENTRY.containing_type = _STATEMACHINE
_STATEMACHINE.fields_by_name['states'].message_type = _STATE
_STATEMACHINE.fields_by_name['assets'].message_type = _STATEMACHINE_ASSETSENTRY
DESCRIPTOR.message_types_by_name['TriggerPredicate'] = _TRIGGERPREDICATE
DESCRIPTOR.message_types_by_name['Processor'] = _PROCESSOR
DESCRIPTOR.message_types_by_name['Transition'] = _TRANSITION
DESCRIPTOR.message_types_by_name['Instruction'] = _INSTRUCTION
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['StateMachine'] = _STATEMACHINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TriggerPredicate = _reflection.GeneratedProtocolMessageType('TriggerPredicate', (_message.Message,), dict(
  DESCRIPTOR = _TRIGGERPREDICATE,
  __module__ = 'proto.wca_state_machine_pb2'
  # @@protoc_insertion_point(class_scope:TriggerPredicate)
  ))
_sym_db.RegisterMessage(TriggerPredicate)

Processor = _reflection.GeneratedProtocolMessageType('Processor', (_message.Message,), dict(
  DESCRIPTOR = _PROCESSOR,
  __module__ = 'proto.wca_state_machine_pb2'
  # @@protoc_insertion_point(class_scope:Processor)
  ))
_sym_db.RegisterMessage(Processor)

Transition = _reflection.GeneratedProtocolMessageType('Transition', (_message.Message,), dict(
  DESCRIPTOR = _TRANSITION,
  __module__ = 'proto.wca_state_machine_pb2'
  # @@protoc_insertion_point(class_scope:Transition)
  ))
_sym_db.RegisterMessage(Transition)

Instruction = _reflection.GeneratedProtocolMessageType('Instruction', (_message.Message,), dict(
  DESCRIPTOR = _INSTRUCTION,
  __module__ = 'proto.wca_state_machine_pb2'
  # @@protoc_insertion_point(class_scope:Instruction)
  ))
_sym_db.RegisterMessage(Instruction)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(
  DESCRIPTOR = _STATE,
  __module__ = 'proto.wca_state_machine_pb2'
  # @@protoc_insertion_point(class_scope:State)
  ))
_sym_db.RegisterMessage(State)

StateMachine = _reflection.GeneratedProtocolMessageType('StateMachine', (_message.Message,), dict(

  AssetsEntry = _reflection.GeneratedProtocolMessageType('AssetsEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATEMACHINE_ASSETSENTRY,
    __module__ = 'proto.wca_state_machine_pb2'
    # @@protoc_insertion_point(class_scope:StateMachine.AssetsEntry)
    ))
  ,
  DESCRIPTOR = _STATEMACHINE,
  __module__ = 'proto.wca_state_machine_pb2'
  # @@protoc_insertion_point(class_scope:StateMachine)
  ))
_sym_db.RegisterMessage(StateMachine)
_sym_db.RegisterMessage(StateMachine.AssetsEntry)


_STATEMACHINE_ASSETSENTRY._options = None
# @@protoc_insertion_point(module_scope)
