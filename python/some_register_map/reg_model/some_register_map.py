"""
Python Wrapper for the some_register_map register model

This code was generated from the PeakRDL-python package version 0.6.4

"""

from typing import Tuple
from typing import Iterator
from typing import List
from typing import Optional
from typing import Union
from typing import cast
from typing import Dict

from typing import Generator

import warnings


from contextlib import contextmanager

from ..lib import AddressMap, RegFile, Memory
from ..lib  import AddressMapArray, RegFileArray

from ..lib import RegReadOnly, RegWriteOnly, RegReadWrite
from ..lib import RegReadOnlyArray, RegWriteOnlyArray, RegReadWriteArray
from ..lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field

from ..lib import ReadableRegister, WritableRegister
from ..lib import ReadableRegisterArray, WritableRegisterArray
from ..lib import FieldSizeProps, FieldMiscProps


from ..lib import NormalCallbackSet















# regfile, register and field definitions
        
    
class some_register_map_chip_id_reg_rev_num_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>This field represents the chips revision number</p>             |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : List[str] = []
    

        
    
class some_register_map_chip_id_reg_part_num_cls(FieldReadOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>This field represents the chips part number</p>                 |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : List[str] = []
    

        
class some_register_map_chip_id_reg_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      This chip part number and revision #                               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>This register cotains the part # and revision # for XYZ         |
    |              |      ASIC</p>                                                           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : List[str] = ['__rev_num', '__part_num']

    def __init__(self,
                 callbacks: NormalCallbackSet,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,Memory]):

        super().__init__(callbacks=callbacks,
                         address=address,
                         accesswidth=32,
                         width=32,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        self.__rev_num:some_register_map_chip_id_reg_rev_num_cls = some_register_map_chip_id_reg_rev_num_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=4,
                lsb=0,
                msb=3,
                low=0,
                high=3),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.rev_num',
            inst_name='rev_num')
        self.__part_num:some_register_map_chip_id_reg_part_num_cls = some_register_map_chip_id_reg_part_num_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=28,
                lsb=4,
                msb=31,
                low=4,
                high=31),
            misc_props=FieldMiscProps(
                default=19088743,
                is_volatile=True),
            logger_handle=logger_handle+'.part_num',
            inst_name='part_num')

    
    @property
    def readable_fields(self) -> Iterator[Union[FieldReadOnly, FieldReadWrite]]:
        """
        generator that produces has all the readable fields within the register
        """
        yield self.rev_num
        yield self.part_num
        

    
    @contextmanager
    def single_read(self) -> Generator['some_register_map_chip_id_reg_cls', None, None]:
        """
        Context Manager to do multiple accesses using a single read operation
        """
        with super().single_read() as reg:
           yield cast('some_register_map_chip_id_reg_cls',reg)

    


    

    

    # build the properties for the fields
    @property
    def rev_num(self) -> some_register_map_chip_id_reg_rev_num_cls:
        """
        Property to access rev_num field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>This field represents the chips revision number</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rev_num
        
    @property
    def part_num(self) -> some_register_map_chip_id_reg_part_num_cls:
        """
        Property to access part_num field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>This field represents the chips part number</p>                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__part_num
        

    @property
    def systemrdl_python_child_name_map(self) -> Dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
            'rev_num':'rev_num',
            'part_num':'part_num',
            }
    

        
    
class some_register_map_enable_enable_cls(FieldWriteOnly):
    
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Enable toggle                                                      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : List[str] = []
    

        
class some_register_map_enable_cls(RegWriteOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      Enable register                                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Toggle the peripheral enable on write</p>                       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : List[str] = ['__enable']

    def __init__(self,
                 callbacks: NormalCallbackSet,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,Memory]):

        super().__init__(callbacks=callbacks,
                         address=address,
                         accesswidth=32,
                         width=32,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        self.__enable:some_register_map_enable_enable_cls = some_register_map_enable_enable_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0,
                msb=0,
                low=0,
                high=0),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.enable',
            inst_name='enable')

    

    
    @property
    def writable_fields(self) -> Iterator[Union[FieldWriteOnly, FieldReadWrite]]:
        """
        generator that produces has all the writable fields within the register
        """
        yield self.enable
        

    
    
    def write_fields(self,enable :int) -> None: # type: ignore[override]
        """
        Do a write to the register, updating all fields
        """
        reg_value = 0
        reg_value |= self.enable.encode_write_value(enable)
        

        self.write(reg_value)

    
    

    # build the properties for the fields
    @property
    def enable(self) -> some_register_map_enable_enable_cls:
        """
        Property to access enable field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Enable toggle                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__enable
        

    @property
    def systemrdl_python_child_name_map(self) -> Dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {
            'enable':'enable',
            }
    

        
class some_register_map_cls(AddressMap):
    """
    Class to represent a address map in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      RDL Example Registers                                              |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>This address map contains some example registers to show how    |
    |              |      RDL can be utilized in various situations.</p>                     |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : List[str] = ['__chip_id_reg', '__enable']

    def __init__(self,
                 callbacks: NormalCallbackSet,
                 address:int=0,
                 logger_handle:str='reg_model.some_register_map',
                 inst_name:str='some_register_map',
                 parent:Optional[AddressMap]=None):

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        
            
        self.__chip_id_reg:some_register_map_chip_id_reg_cls = some_register_map_chip_id_reg_cls(callbacks=callbacks,
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.chip_id_reg',
                                                                                       inst_name='chip_id_reg', parent=self)
        
            
        self.__enable:some_register_map_enable_cls = some_register_map_enable_cls(callbacks=callbacks,
                                                                                     address=self.address+4,
                                                                                     logger_handle=logger_handle+'.enable',
                                                                                     inst_name='enable', parent=self)
        
    @property
    def chip_id_reg(self) -> some_register_map_chip_id_reg_cls:
        """
        Property to access chip_id_reg 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      This chip part number and revision #                               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>This register cotains the part # and revision # for XYZ         |
        |              |      ASIC</p>                                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__chip_id_reg
        
    @property
    def enable(self) -> some_register_map_enable_cls:
        """
        Property to access enable 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      Enable register                                                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Toggle the peripheral enable on write</p>                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__enable
        

    @property
    def systemrdl_python_child_name_map(self) -> Dict[str, str]:
        """
        In some cases systemRDL names need to be converted make them python safe, this dictionary
        is used to map the original systemRDL names to the names of the python attributes of this
        class

        Returns: dictionary whose key is the systemRDL names and value it the property name
        """
        return {'chip_id_reg':'chip_id_reg','enable':'enable',
            }

    

    def get_readable_registers(self, unroll:bool=False) -> Iterator[Union[ReadableRegister, Tuple[ReadableRegister, ...]]]:
        """
        generator that produces all the readable_registers of this node
        """
        
                
                    
        yield cast(ReadableRegister, self.chip_id_reg)
                

        # Empty generator in case there are no children of this type
        if False: yield

    def get_writable_registers(self, unroll:bool=False) -> Iterator[Union[WritableRegister, Tuple[WritableRegister, ...]]]:
        """
        generator that produces all the readable_registers of this node
        """
        
                
                
                    
        yield cast(WritableRegister, self.enable)

        # Empty generator in case there are no children of this type
        if False: yield
    
    def get_memories(self, unroll:bool=False) -> Iterator[Union[Memory,Tuple[Memory,...]]]:
        """
        generator that produces all the Memory children of this node
        """
        

        # Empty generator in case there are no children of this type
        if False: yield
    
    def get_sections(self, unroll:bool=False) -> Iterator[Union[Union[AddressMap, RegFile],Tuple[Union[AddressMap, RegFile],...]]]:
        """
        generator that produces all the Union[AddressMap, RegFile] children of this node
        """
        

        # Empty generator in case there are no children of this type
        if False: yield
    



if __name__ == '__main__':
    # dummy functions to demonstrate the class
    def read_addr_space(addr: int, width: int, accesswidth: int) -> int:
        """
        Callback to simulate the operation of the package, everytime the read is called, it will
        request the user input the value to be read back.

        Args:
            addr: Address to write to
            width: Width of the register in bits
            accesswidth: Minimum access width of the register in bits

        Returns:
            value inputted by the used
        """
        assert isinstance(addr, int)
        assert isinstance(width, int)
        assert isinstance(accesswidth, int)
        return int(input('value to read from address:0x%X'%addr))

    def write_addr_space(addr: int, width: int, accesswidth: int, data: int) -> None:
        """
        Callback to simulate the operation of the package, everytime the read is called, it will
        request the user input the value to be read back.

        Args:
            addr: Address to write to
            width: Width of the register in bits
            accesswidth: Minimum access width of the register in bits
            data: value to be written to the register

        Returns:
            None
        """
        assert isinstance(addr, int)
        assert isinstance(width, int)
        assert isinstance(accesswidth, int)
        assert isinstance(data, int)
        print('write data:0x%X to address:0x%X'%(data, addr))

    # create an instance of the class
    some_register_map = some_register_map_cls(callbacks = NormalCallbackSet(read_callback=read_addr_space,
                                                                                                     write_callback=write_addr_space))