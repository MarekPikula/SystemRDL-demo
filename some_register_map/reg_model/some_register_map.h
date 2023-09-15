/* ------------------------------------------------------------------------------------------------
C Headers for the some_register_map register model

This code was generated from the PeakRDL-CHeader package
------------------------------------------------------------------------------------------------ */#ifndef _SOME_REGISTER_MAP_REGS_H_
#define _SOME_REGISTER_MAP_REGS_H_
        
/* ------------------------------------------------------------------------------------------------
Field definition for: some_register_map_chip_id_reg_rev_num

+--------------+-------------------------------------------------------------------------+
| SystemRDL    | Value                                                                   |
| Field        |                                                                         |
+==============+=========================================================================+
| Description  | .. raw:: html                                                           |
|              |                                                                         |
|              |      <p>This field represents the chips revision number</p>             |
+--------------+-------------------------------------------------------------------------+
------------------------------------------------------------------------------------------------ */
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_LSB 0U
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_MSB 3U
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_LOW 0U
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_HIGH 3U
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_MASK 0xFU
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_INVMASK 0xFFFFFFF0U
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_SIZE 4U


        
/* ------------------------------------------------------------------------------------------------
Field definition for: some_register_map_chip_id_reg_part_num

+--------------+-------------------------------------------------------------------------+
| SystemRDL    | Value                                                                   |
| Field        |                                                                         |
+==============+=========================================================================+
| Description  | .. raw:: html                                                           |
|              |                                                                         |
|              |      <p>This field represents the chips part number</p>                 |
+--------------+-------------------------------------------------------------------------+
------------------------------------------------------------------------------------------------ */
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_LSB 4U
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_MSB 31U
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_LOW 4U
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_HIGH 31U
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_MASK 0xFFFFFFF0U
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_INVMASK 0xFU
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_SIZE 28U


        
/* ------------------------------------------------------------------------------------------------
Register definition for: some_register_map_chip_id_reg

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
------------------------------------------------------------------------------------------------ */
#define DEF_SOME_REGISTER_MAP_CHIP_ID_REG_SIZE 4U

        
/* ------------------------------------------------------------------------------------------------
Field definition for: some_register_map_enable_enable

+--------------+-------------------------------------------------------------------------+
| SystemRDL    | Value                                                                   |
| Field        |                                                                         |
+==============+=========================================================================+
| Name         | .. raw:: html                                                           |
|              |                                                                         |
|              |      Enable toggle                                                      |
+--------------+-------------------------------------------------------------------------+
------------------------------------------------------------------------------------------------ */
#define DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_LSB 0U
#define DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_MSB 0U
#define DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_LOW 0U
#define DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_HIGH 0U
#define DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_MASK 0x1U
#define DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_INVMASK 0xFFFFFFFEU
#define DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_SIZE 1U


        
/* ------------------------------------------------------------------------------------------------
Register definition for: some_register_map_enable

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
------------------------------------------------------------------------------------------------ */
#define DEF_SOME_REGISTER_MAP_ENABLE_SIZE 4U

        
/* ------------------------------------------------------------------------------------------------
Address definition for: some_register_map

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
------------------------------------------------------------------------------------------------ */

    
// Register chip_id_reg
#define SOME_REGISTER_MAP_CHIP_ID_REG_ADDRESS 0U
#define SOME_REGISTER_MAP_CHIP_ID_REG_SIZE DEF_SOME_REGISTER_MAP_CHIP_ID_REG_SIZE // size in bytes
// Fields in Register chip_id_reg
#define SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_LSB DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_LSB
#define SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_MSB DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_MSB
#define SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_LOW DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_LOW
#define SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_HIGH DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_HIGH
#define SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_MASK DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_MASK
#define SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_INVMASK DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_INVMASK
#define SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_SIZE DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_SIZE // size in bits
#define SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_DEFAULT DEF_SOME_REGISTER_MAP_CHIP_ID_REG_REV_NUM_DEFAULT
#define SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_LSB DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_LSB
#define SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_MSB DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_MSB
#define SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_LOW DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_LOW
#define SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_HIGH DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_HIGH
#define SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_MASK DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_MASK
#define SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_INVMASK DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_INVMASK
#define SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_SIZE DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_SIZE // size in bits
#define SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_DEFAULT DEF_SOME_REGISTER_MAP_CHIP_ID_REG_PART_NUM_DEFAULT
    
// Register enable
#define SOME_REGISTER_MAP_ENABLE_ADDRESS 4U
#define SOME_REGISTER_MAP_ENABLE_SIZE DEF_SOME_REGISTER_MAP_ENABLE_SIZE // size in bytes
// Fields in Register enable
#define SOME_REGISTER_MAP_ENABLE_ENABLE_LSB DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_LSB
#define SOME_REGISTER_MAP_ENABLE_ENABLE_MSB DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_MSB
#define SOME_REGISTER_MAP_ENABLE_ENABLE_LOW DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_LOW
#define SOME_REGISTER_MAP_ENABLE_ENABLE_HIGH DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_HIGH
#define SOME_REGISTER_MAP_ENABLE_ENABLE_MASK DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_MASK
#define SOME_REGISTER_MAP_ENABLE_ENABLE_INVMASK DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_INVMASK
#define SOME_REGISTER_MAP_ENABLE_ENABLE_SIZE DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_SIZE // size in bits
#define SOME_REGISTER_MAP_ENABLE_ENABLE_DEFAULT DEF_SOME_REGISTER_MAP_ENABLE_ENABLE_DEFAULT

#endif /* _SOME_REGISTER_MAP_REGS_H_ */