"""Python abstraction for SystemRDL register description.

Don't override. Generated from:
    example.rdl
"""

from peakrdl_python_simple.regif import access, spec


class ChipIdReg(access.RegAccess):
    """This chip part number and revision #

    This register cotains the part # and revision # for XYZ ASIC
    """

    rev_num = access.FieldAccess(specification=spec.FieldNodeSpec(inst_name='rev_num', type_name='rev_num', orig_type_name=None, external=False, width=4, msb=3, lsb=0, high=3, low=0, is_virtual=False, is_volatile=False, is_sw_writable=False, is_sw_readable=True, is_hw_writable=False, is_hw_readable=False, implements_storage=False, is_up_counter=False, is_down_counter=False, encode='int'), field_type=int)
    """This field represents the chips revision number"""

    part_num = access.FieldAccess(specification=spec.FieldNodeSpec(inst_name='part_num', type_name='part_num', orig_type_name=None, external=False, width=28, msb=31, lsb=4, high=31, low=4, is_virtual=False, is_volatile=True, is_sw_writable=False, is_sw_readable=True, is_hw_writable=True, is_hw_readable=False, implements_storage=False, is_up_counter=False, is_down_counter=False, encode='int'), field_type=int)
    """This field represents the chips part number"""


class enableReg(access.RegAccess):
    """Enable register

    Toggle the peripheral enable on write
    """

    enable = access.FieldAccess(specification=spec.FieldNodeSpec(inst_name='enable', type_name='enable', orig_type_name=None, external=False, width=1, msb=0, lsb=0, high=0, low=0, is_virtual=False, is_volatile=False, is_sw_writable=True, is_sw_readable=False, is_hw_writable=False, is_hw_readable=True, implements_storage=True, is_up_counter=False, is_down_counter=False, encode='bool'), field_type=bool)
    """Enable toggle"""


class SomeRegisterMapAddrmap(access.AddrmapAccess):
    """RDL Example Registers

    This address map contains some example registers to show
    how RDL can be utilized in various situations.
    """

    _spec = spec.AddrmapNodeSpec(inst_name='some_register_map', type_name='some_register_map', orig_type_name='some_register_map', external=True, raw_address_offset=0, address_offset=0, raw_absolute_address=0, absolute_address=0, size=8, total_size=8, is_array=False, array_dimensions=None, array_stride=None)
    chip_id_reg = ChipIdReg(specification=spec.RegNodeSpec(inst_name='chip_id_reg', type_name='chip_id_reg', orig_type_name=None, external=False, raw_address_offset=0, address_offset=0, raw_absolute_address=0, absolute_address=0, size=4, total_size=4, is_array=False, array_dimensions=None, array_stride=None, is_virtual=False, has_sw_writable=False, has_sw_readable=True, has_hw_writable=True, has_hw_readable=False, is_interrupt_reg=False, is_halt_reg=False, field_count=2))
    """This chip part number and revision #

    This register cotains the part # and revision # for XYZ ASIC
    """

    enable = enableReg(specification=spec.RegNodeSpec(inst_name='enable', type_name='enable', orig_type_name=None, external=False, raw_address_offset=4, address_offset=4, raw_absolute_address=4, absolute_address=4, size=4, total_size=4, is_array=False, array_dimensions=None, array_stride=None, is_virtual=False, has_sw_writable=True, has_sw_readable=False, has_hw_writable=False, has_hw_readable=True, is_interrupt_reg=False, is_halt_reg=False, field_count=1))
    """Enable register

    Toggle the peripheral enable on write
    """
