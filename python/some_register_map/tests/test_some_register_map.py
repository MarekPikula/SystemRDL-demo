"""
Unit Tests for the some_register_map register model Python Wrapper

This code was generated from the PeakRDL-python package version 0.6.4
"""
from typing import List, Union, Dict
from array import array as Array

import unittest
from unittest.mock import patch, call

import random
from itertools import combinations
import math
from enum import IntEnum

from ..lib import RegisterWriteVerifyError

from ..reg_model.some_register_map import some_register_map_cls

from ..lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite
from ..lib import WritableRegister, ReadableRegister, RegReadWrite, RegReadOnly, RegWriteOnly
from ..lib import MemoryReadOnly, MemoryWriteOnly, MemoryReadWrite

from ..lib import AddressMap, RegFile
from ..lib import Memory
from ..lib import Field
from ..lib import Reg

from ._some_register_map_test_base import some_register_map_TestCase, some_register_map_TestCase_BlockAccess
from ._some_register_map_test_base import __name__ as base_name

class some_register_map_single_access(some_register_map_TestCase): # type: ignore[valid-type,misc]

    def test_inst_name(self)  -> None:
        """
        Walk the address map and check the inst name has been correctly populated
        """
        with self.subTest(msg='node: some_register_map.chip_id_reg'):
            self.assertEqual(self.dut.chip_id_reg.inst_name, 'chip_id_reg') # type: ignore[union-attr]
            self.assertEqual(self.dut.chip_id_reg.full_inst_name, 'some_register_map.chip_id_reg')  # type: ignore[union-attr]
        with self.subTest(msg='node: some_register_map.enable'):
            self.assertEqual(self.dut.enable.inst_name, 'enable') # type: ignore[union-attr]
            self.assertEqual(self.dut.enable.full_inst_name, 'some_register_map.enable')  # type: ignore[union-attr]
        with self.subTest(msg='node: some_register_map.chip_id_reg.rev_num'):
            self.assertEqual(self.dut.chip_id_reg.rev_num.inst_name, 'rev_num') # type: ignore[union-attr]
            self.assertEqual(self.dut.chip_id_reg.rev_num.full_inst_name, 'some_register_map.chip_id_reg.rev_num')  # type: ignore[union-attr]
        with self.subTest(msg='node: some_register_map.chip_id_reg.part_num'):
            self.assertEqual(self.dut.chip_id_reg.part_num.inst_name, 'part_num') # type: ignore[union-attr]
            self.assertEqual(self.dut.chip_id_reg.part_num.full_inst_name, 'some_register_map.chip_id_reg.part_num')  # type: ignore[union-attr]
        with self.subTest(msg='node: some_register_map.enable.enable'):
            self.assertEqual(self.dut.enable.enable.inst_name, 'enable') # type: ignore[union-attr]
            self.assertEqual(self.dut.enable.enable.full_inst_name, 'some_register_map.enable.enable')  # type: ignore[union-attr]
        

    def test_register_properties(self)  -> None:
        """
        Walk the address map and check the address, size and accesswidth of every register is
        correct
        """
        with self.subTest(msg='register: some_register_map.chip_id_reg'):
            self.assertEqual(self.dut.chip_id_reg.address, 0) # type: ignore[union-attr]
            self.assertEqual(self.dut.chip_id_reg.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.chip_id_reg.accesswidth, self.dut.chip_id_reg.accesswidth) # type: ignore[union-attr]
        with self.subTest(msg='register: some_register_map.enable'):
            self.assertEqual(self.dut.enable.address, 4) # type: ignore[union-attr]
            self.assertEqual(self.dut.enable.width, 32) # type: ignore[union-attr]
            self.assertEqual(self.dut.enable.accesswidth, self.dut.enable.accesswidth) # type: ignore[union-attr]
        

    def test_memory_properties(self)  -> None:
        """
        Walk the address map and check the address, size and accesswidth of every memory is
        correct
        """
        mut: Memory
        

    def test_field_properties(self)  -> None:
        """
        walk the address map and check:
        - that the lsb and msb of every field is correct
        - that where default values are provided they are applied correctly
        """
        fut:Field
        with self.subTest(msg='field: some_register_map.chip_id_reg.rev_num'):
            # test properties of field: some_register_map.chip_id_reg.rev_num
            fut = self.dut.chip_id_reg.rev_num # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,3)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,3)
            self.assertEqual(fut.bitmask,0xF)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFF0)
            self.assertEqual(fut.max_value,0xF)
                
            self.assertEqual(fut.default,1)
                
            self.assertEqual(fut.is_volatile,False)
        with self.subTest(msg='field: some_register_map.chip_id_reg.part_num'):
            # test properties of field: some_register_map.chip_id_reg.part_num
            fut = self.dut.chip_id_reg.part_num # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,4)
            self.assertEqual(fut.msb,31)
            self.assertEqual(fut.low,4)
            self.assertEqual(fut.high,31)
            self.assertEqual(fut.bitmask,0xFFFFFFF0)
            self.assertEqual(fut.inverse_bitmask,0xF)
            self.assertEqual(fut.max_value,0xFFFFFFF)
                
            self.assertEqual(fut.default,19088743)
                
            self.assertEqual(fut.is_volatile,True)
        with self.subTest(msg='field: some_register_map.enable.enable'):
            # test properties of field: some_register_map.enable.enable
            fut = self.dut.enable.enable # type: ignore[union-attr]
            if not isinstance(fut, Field):
                raise TypeError('This test relies on node being of type Field')
            self.assertEqual(fut.lsb,0)
            self.assertEqual(fut.msb,0)
            self.assertEqual(fut.low,0)
            self.assertEqual(fut.high,0)
            self.assertEqual(fut.bitmask,0x1)
            self.assertEqual(fut.inverse_bitmask,0xFFFFFFFE)
            self.assertEqual(fut.max_value,0x1)
                
            self.assertEqual(fut.default,None)
                
            self.assertEqual(fut.is_volatile,False)
        

    def test_register_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        rut: Reg
        # test access operations (read and/or write) to register:
        # some_register_map.chip_id_reg
        with self.subTest(msg='register: some_register_map.chip_id_reg'):
            rut=self.dut.chip_id_reg # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                
                if not isinstance(rut, (RegReadOnly, RegReadWrite)):
                    raise TypeError('Register is not a Readable Type')
                
                # test reading back 1 (the unpatched version returns 0 so this confirms the patch works)
                self.assertEqual(rut.read(), 1)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read check with high value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFFF
                self.assertEqual(rut.read(), 0xFFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of the low value
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0
                self.assertEqual(rut.read(), 0x0)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # test the read of a random value
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = random_value
                self.assertEqual(rut.read(), random_value)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=rut.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()
                

                
                # test that a non-writable register has no write method and attempting one generates and error
                with self.assertRaises(AttributeError):
                    rut.write(0) # type: ignore[attr-defined]

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        # test access operations (read and/or write) to register:
        # some_register_map.enable
        with self.subTest(msg='register: some_register_map.enable'):
            rut=self.dut.enable # type: ignore[union-attr,assignment]
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock:

                

                
                if not isinstance(rut, (RegWriteOnly, RegReadWrite)):
                    raise TypeError('Register is not a Writeable Type')
                
                # test the write with high value
                rut.write(0xFFFFFFFF)
                write_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0xFFFFFFFF)
                write_callback_mock.reset_mock()

                # test the write of a low value
                rut.write(0)
                write_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=0)
                write_callback_mock.reset_mock()

                # test the write of a random
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                rut.write(random_value)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=rut.accesswidth,
                                    data=random_value)
                write_callback_mock.reset_mock()

                # test writting a value beyond the register range is blocked with an exception being raised
                with self.assertRaises(ValueError):
                    rut.write(-1)

                with self.assertRaises(ValueError):
                    rut.write(0xFFFFFFFF+1)

                # check the read has not been called in the write test
                read_callback_mock.assert_not_called()
        

    def test_int_field_read_and_write(self) -> None:
        """
        Check the ability to read and write to integer (non-eumn) fields
        """
        fut:Field
        

        # test access operations (read and/or write) to field:
        # some_register_map.chip_id_reg.rev_num
        with self.subTest(msg='field: some_register_map.chip_id_reg.rev_num'):
            fut = self.dut.chip_id_reg.rev_num # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldReadOnly, FieldReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xFFFFFFF0
                self.assertEqual(fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xF
                self.assertEqual(fut.read(),
                                 0xF)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xF) >> 0
                self.assertEqual(fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()

        # test access operations (read and/or write) to field:
        # some_register_map.chip_id_reg.part_num
        with self.subTest(msg='field: some_register_map.chip_id_reg.part_num'):
            fut = self.dut.chip_id_reg.part_num # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                
                if not isinstance(fut, (FieldReadOnly, FieldReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a readable field')
                

                # read back - zero, this is achieved by setting the register to inverse bitmask
                read_callback_mock.return_value = 0xF
                self.assertEqual(fut.read(),
                                 0)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - max_value, this is achieved by setting the register to bitmask
                read_callback_mock.reset_mock()
                read_callback_mock.return_value = 0xFFFFFFF0
                self.assertEqual(fut.read(),
                                 0xFFFFFFF)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # read back - random value
                read_callback_mock.reset_mock()
                random_value = random.randrange(0, 0xFFFFFFFF+1)
                read_callback_mock.return_value = random_value
                random_field_value = (random_value & 0xFFFFFFF0) >> 4
                self.assertEqual(fut.read(),
                                 random_field_value)
                read_callback_mock.assert_called_once_with(
                                    addr=0,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth)

                # at the end of the read tests the write should not have been called
                read_callback_mock.reset_mock()
                write_callback_mock.assert_not_called()

        # test access operations (read and/or write) to field:
        # some_register_map.enable.enable
        with self.subTest(msg='field: some_register_map.enable.enable'):
            fut = self.dut.enable.enable # type: ignore[union-attr]
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:

                
                # check the write
                
                if not isinstance(fut, (FieldWriteOnly, FieldReadWrite)):
                    raise TypeError('Test can not proceed as the fut is not a writable field')
                

                random_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                random_field_value = random.randrange(0, 0x1 + 1)
                for reg_base_value in [0, 0xFFFFFFFF, random_reg_value]:
                    for field_value in [0, 0x1, random_field_value]:
                        read_callback_mock.reset_mock()
                        write_callback_mock.reset_mock()
                        read_callback_mock.return_value = reg_base_value

                        self.dut.enable.enable.write(field_value) # type: ignore[union-attr]

                        
                        read_callback_mock.assert_not_called()
                        # if the register is not readable, the value is simply written
                        write_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=fut.parent_register.accesswidth,
                                    data=field_value << 0)
                        

                # check invalid write values bounce
                with self.assertRaises(ValueError):
                    fut.write(0x1 + 1)

                with self.assertRaises(ValueError):
                    fut.write(-1)

    

    def test_register_read_fields(self) -> None:
        """
        Walk the register map and check every register read_fields method
        """
        reference_read_fields: Dict[str, Union[bool, IntEnum, int]]
        
        with self.subTest(msg='register: some_register_map.chip_id_reg'):
            # test read_fields to register:
            # some_register_map.chip_id_reg
            # build up the register value with a random base value, overlaid with
            # a random value for each field
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFF0) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xF) | (rand_field_value << 4)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:
                # the read_fields method gets a dictionary back
                # from the object with all the read back field
                # values
                reference_read_fields = { 
                                          'rev_num' : self.dut.chip_id_reg.rev_num.read(), # type: ignore[union-attr]
                                          'part_num' : self.dut.chip_id_reg.part_num.read() # type: ignore[union-attr]
                                        }

                read_callback_mock.reset_mock()

                self.assertDictEqual(self.dut.chip_id_reg.read_fields(), # type: ignore[union-attr]
                                     reference_read_fields)
                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()

    def test_register_read_context_manager(self) -> None:
        """
        Walk the register map and check every register read_fields method
        """
        reference_read_fields: Dict[str, Union[bool, IntEnum, int]]
        
        # test context manager to register:
        # some_register_map.chip_id_reg
        # build up the register value with a random base value, overlaid with
        # a random value for each field
        with self.subTest(msg='register: some_register_map.chip_id_reg'):
            rand_reg_value = random.randrange(0, 0xFFFFFFFF + 1)
                
                    
                        
            rand_field_value = random.randrange(0, 0xF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xFFFFFFF0) | (rand_field_value << 0)
                        
                    
                
            
                
                    
                        
            rand_field_value = random.randrange(0, 0xFFFFFFF + 1)
                        
                        
            rand_reg_value = (rand_reg_value & 0xF) | (rand_field_value << 4)
                        
                    
                
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                 patch(base_name + '.read_addr_space', return_value=rand_reg_value) as read_callback_mock:

                # first read the fields using the "normal" method, then compare the result to reading
                # via the context manager
                reference_read_fields = { 
                                          'rev_num' : self.dut.chip_id_reg.rev_num.read(),  # type: ignore[union-attr]
                                          'part_num' : self.dut.chip_id_reg.part_num.read()  # type: ignore[union-attr]
                                        }
                read_callback_mock.reset_mock()

                
                with self.dut.chip_id_reg.single_read() as reg_context: # type: ignore[union-attr]
                    self.assertEqual(reference_read_fields['rev_num'],
                                     reg_context.get_child_by_system_rdl_name('rev_num').read())  # type: ignore[attr-defined,union-attr]
                    self.assertEqual(reference_read_fields['part_num'],
                                     reg_context.get_child_by_system_rdl_name('part_num').read())  # type: ignore[attr-defined,union-attr]

                read_callback_mock.assert_called_once()
                write_callback_mock.assert_not_called()

    def test_register_write_context_manager(self) -> None:
        """
        Test the read modify write context manager
        """
        rut:RegReadWrite
        def write_field_cominbinations(reg: RegReadWrite, writable_fields:List[str]) -> None:
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:
                for num_parm in range(1, len(writable_fields) + 1):
                    for fields_to_write in combinations(writable_fields, num_parm):
                        field_values = {}
                        expected_value = 0
                        for field_str in fields_to_write:
                            field = getattr(reg, field_str)
                            if hasattr(field, 'enum_cls'):
                                rand_enum_value = random.choice(list(field.enum_cls))
                                rand_field_value = rand_enum_value.value   # type: ignore[attr-defined]
                                field_values[field_str] = rand_enum_value
                            else:
                                rand_field_value = random.randrange(0, field.max_value + 1)
                                field_values[field_str] = rand_field_value

                            if field.msb == field.high:
                                expected_value = ( expected_value & field.inverse_bitmask ) | (rand_field_value << field.low)
                            elif field.msb == field.low:
                                expected_value = ( expected_value & field.inverse_bitmask ) | (self._reverse_bits(value=rand_field_value, number_bits=field.width) << field.low)
                            else:
                                raise RuntimeError('invalid msb/lsb high/low combination')

                        # read/write without verify
                        read_callback_mock.return_value = 0
                        with reg.single_read_modify_write(verify=False) as reg_session:
                            for field_name, field_value in field_values.items():
                                field = getattr(reg_session, field_name)
                                field.write(field_value)

                        write_callback_mock.assert_called_once_with(
                                addr=reg.address,
                                width=reg.width,
                                accesswidth=reg.accesswidth,
                                data=expected_value)
                        read_callback_mock.assert_called_once()
                        write_callback_mock.reset_mock()
                        read_callback_mock.reset_mock()

                        # read/write/verify pass
                        with reg.single_read_modify_write(verify=True) as reg_session:
                            for field_name, field_value in field_values.items():
                                field = getattr(reg_session, field_name)
                                field.write(field_value)
                            read_callback_mock.return_value = expected_value

                        write_callback_mock.assert_called_once_with(
                                addr=reg.address,
                                width=reg.width,
                                accesswidth=reg.accesswidth,
                                data=expected_value)
                        self.assertEqual(read_callback_mock.call_count, 2)
                        write_callback_mock.reset_mock()
                        read_callback_mock.reset_mock()

                        # read/write/verify pass
                        with self.assertRaises(RegisterWriteVerifyError) as context:
                            with reg.single_read_modify_write(verify=True) as reg_session:
                                for field_name, field_value in field_values.items():
                                    field = getattr(reg_session, field_name)
                                    field.write(field_value)
                                read_callback_mock.return_value = expected_value ^ reg_session.max_value

                        write_callback_mock.reset_mock()
                        read_callback_mock.reset_mock()

        

    def test_register_write_fields(self) -> None:
        """
        Walk the register map and check every register write_fields method
        """
        rut:RegReadWrite
        rand_enum_value:IntEnum
        def write_field_cominbinations(reg: RegReadWrite, writable_fields:List[str]) -> None:
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:
                for num_parm in range(1, len(writable_fields) + 1):
                    for fields_to_write in combinations(writable_fields, num_parm):
                        kwargs = {}
                        expected_value = 0
                        for field_str in fields_to_write:
                            field = getattr(reg, field_str)
                            if hasattr(field, 'enum_cls'):
                                rand_enum_value = random.choice(list(field.enum_cls))
                                rand_field_value = rand_enum_value.value   # type: ignore[attr-defined]
                                kwargs[field_str] = rand_enum_value
                            else:
                                rand_field_value = random.randrange(0, field.max_value + 1)
                                kwargs[field_str] = rand_field_value

                            if field.msb == field.high:
                                expected_value = ( expected_value & field.inverse_bitmask ) | (rand_field_value << field.low)
                            elif field.msb == field.low:
                                expected_value = ( expected_value & field.inverse_bitmask ) | (self._reverse_bits(value=rand_field_value, number_bits=field.width) << field.low)
                            else:
                                raise RuntimeError('invalid msb/lsb high/low combination')

                        reg.write_fields(**kwargs)
                        write_callback_mock.assert_called_once_with(
                                addr=reg.address,
                                width=reg.width,
                                accesswidth=reg.accesswidth,
                                data=expected_value)
                        read_callback_mock.assert_called_once()
                        write_callback_mock.reset_mock()
                        read_callback_mock.reset_mock()


        
        with self.subTest(msg='register: some_register_map.enable'):
            # test read_fields to register:
            # some_register_map.enable


            
            kwargs = {} # type: ignore[var-annotated]
            expected_value = 0
            
            rand_field_value = random.randrange(0, 0x1 + 1)
            kwargs['enable'] = rand_field_value
            expected_value = ( expected_value & 0xFFFFFFFE ) | (rand_field_value << 0)
            
            with patch(base_name + '.write_addr_space') as write_callback_mock, \
                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock:
                self.dut.enable.write_fields(**kwargs)  # type: ignore[union-attr]
                write_callback_mock.assert_called_once_with(
                                    addr=4,
                                    width=32,
                                    accesswidth=self.dut.enable.accesswidth, # type: ignore[union-attr]
                                    data=expected_value)
                read_callback_mock.assert_not_called()
                write_callback_mock.reset_mock()
                read_callback_mock.reset_mock()

            

    

    def test_adding_attributes(self) -> None:
        """
        Walk the address map and attempt to set a new value on each node

        The attribute name: cppkbrgmgeloagvfgjjeiiushygirh was randomly generated to be unlikely to
        every be a attribute name

        """
        with self.subTest(msg='node: some_register_map.chip_id_reg'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.chip_id_reg.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: some_register_map.enable'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.enable.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: some_register_map.chip_id_reg.rev_num'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.chip_id_reg.rev_num.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: some_register_map.chip_id_reg.part_num'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.chip_id_reg.part_num.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        with self.subTest(msg='node: some_register_map.enable.enable'):
            with self.assertRaises(AttributeError):
                # this line is trying to set an illegal value so by definition should fail the type
                # checks
                self.dut.enable.enable.cppkbrgmgeloagvfgjjeiiushygirh = 1 # type: ignore[attr-defined,union-attr]
        

    

    

    

    

    def test_traversal_iterators(self) -> None:
        """
        Walk the address map and check that the iterators for each node as as expected
        """
        
        expected_writable_fields: List[Union[FieldWriteOnly, FieldReadWrite]]
        expected_readable_fields: List[Union[FieldReadOnly, FieldReadWrite]]
        expected_writable_regs: List[WritableRegister]
        expected_readable_regs: List[ReadableRegister]
        expected_memories:List[Union[MemoryReadOnly, MemoryWriteOnly, MemoryReadWrite]]
        
        expected_sections : List[Union[AddressMap, RegFile]]

        # test all the registers
        with self.subTest(msg='register: some_register_map.chip_id_reg'):
                
                
            # register should not have writable_fields attribute
            self.assertFalse(hasattr(self.dut.chip_id_reg, 'writable_fields')) # type: ignore[union-attr]
                    
                    
            expected_readable_fields = [self.dut.chip_id_reg.rev_num, # type: ignore[union-attr,list-item] 
                                         self.dut.chip_id_reg.part_num, # type: ignore[union-attr,list-item] 
                                         
                                         ]
            readable_fields = []
            for readable_field in self.dut.chip_id_reg.readable_fields: # type: ignore[union-attr]
                readable_fields.append(readable_field)
            self.assertCountEqual(expected_readable_fields, readable_fields)
                    
        with self.subTest(msg='register: some_register_map.enable'):
                
                
            expected_writable_fields = [self.dut.enable.enable, # type: ignore[union-attr,list-item] 
                                         
                                         ]
            writable_fields = []
            for writable_field in self.dut.enable.writable_fields:  # type: ignore[union-attr]
                writable_fields.append(writable_field)
            self.assertCountEqual(expected_writable_fields, writable_fields)
                    
                    
            # register should not have readable_fields attribute
            self.assertFalse(hasattr(self.dut.enable, 'readable_fields')) # type: ignore[union-attr]
                    
        
        # test all the memories
        
        # test all the address maps
        
        # test all the register files
        

    def test_name_map(self) -> None:
        """
        Check that the function for getting a node by its original systemRDL name works
        """
        
        
        self.assertEqual(self.dut.chip_id_reg.get_child_by_system_rdl_name('rev_num').inst_name, 'rev_num')  # type: ignore[union-attr]
        
        
        
        self.assertEqual(self.dut.chip_id_reg.get_child_by_system_rdl_name('part_num').inst_name, 'part_num')  # type: ignore[union-attr]
        
        
        
        
        self.assertEqual(self.dut.enable.get_child_by_system_rdl_name('enable').inst_name, 'enable')  # type: ignore[union-attr]
        
        
        
        
        
        

class some_register_map_block_access(some_register_map_TestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    


if __name__ == '__main__':

    unittest.main()




