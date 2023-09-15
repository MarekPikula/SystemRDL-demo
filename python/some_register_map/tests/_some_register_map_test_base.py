"""
Unit Tests for the some_register_map register model Python Wrapper

This code was generated from the PeakRDL-python package version 0.6.4
"""
from array import array as Array

import unittest



from ..lib import RegisterWriteVerifyError

from ..lib import NormalCallbackSet



from ..reg_model.some_register_map import some_register_map_cls


# dummy functions to support the test cases, note that these are not used as
# they get patched
def read_addr_space(addr: int, width: int, accesswidth: int) -> int:
    assert isinstance(addr, int)
    assert isinstance(width, int)
    assert isinstance(accesswidth, int)
    
    return 0

def write_addr_space(addr: int, width: int, accesswidth: int,  data: int) -> None:
    assert isinstance(addr, int)
    assert isinstance(width, int)
    assert isinstance(accesswidth, int)
    assert isinstance(data, int)
    

def read_callback(addr: int, width: int, accesswidth: int) -> int:
    return read_addr_space(addr=addr, width=width, accesswidth=accesswidth)

def read_block_addr_space(addr: int, width: int, accesswidth: int, length:int) -> Array:
    assert isinstance(addr, int)
    assert isinstance(width, int)
    assert isinstance(accesswidth, int)
    assert isinstance(length, int)

    if width == 32:
        typecode = 'L'
    elif width == 64:
        typecode = 'Q'
    elif width == 16:
        typecode = 'I'
    elif width == 8:
        typecode = 'B'
    else:
        raise ValueError('unhandled memory width')

    
    return Array(typecode, [0 for x in range(length)])

def read_block_callback(addr: int, width: int, accesswidth: int, length: int) -> Array:
    return read_block_addr_space(addr=addr, width=width, accesswidth=accesswidth, length=length)

def write_callback(addr: int, width: int, accesswidth: int,  data: int) -> None:
    write_addr_space(addr=addr, width=width, accesswidth=accesswidth, data=data)

def write_block_addr_space(addr: int, width: int, accesswidth: int,  data: Array) -> None:
    assert isinstance(addr, int)
    assert isinstance(width, int)
    assert isinstance(accesswidth, int)
    assert isinstance(data, Array)
    

def write_block_callback(addr: int, width: int, accesswidth: int,  data: Array) -> None:
    write_block_addr_space(addr=addr, width=width, accesswidth=accesswidth, data=data)


TestCaseBase = unittest.TestCase


class some_register_map_TestCase(TestCaseBase): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.dut = some_register_map_cls(NormalCallbackSet(read_callback=read_callback,
                                                          write_callback=write_callback))

    @staticmethod
    def _reverse_bits(value: int, number_bits: int) -> int:
        """

        Args:
            value: value to reverse
            number_bits: number of bits used in the value

        Returns:
            reversed valued
        """
        result = 0
        for i in range(number_bits):
            if (value >> i) & 1:
                result |= 1 << (number_bits - 1 - i)
        return result

class some_register_map_TestCase_BlockAccess(TestCaseBase): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.dut = some_register_map_cls(NormalCallbackSet(read_callback=read_callback,
                                                          write_callback=write_callback,
                                                          read_block_callback=read_block_callback,
                                                          write_block_callback=write_block_callback))




if __name__ == '__main__':
    pass



