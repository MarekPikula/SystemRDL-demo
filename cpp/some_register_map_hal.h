// Generated with PeakRD-halcpp : https://github.com/Risto97/PeakRDL-halcpp
// By user: marek-pikula at: 2023-09-16 01:20:43

#ifndef __SOME_REGISTER_MAP_HAL_H_
#define __SOME_REGISTER_MAP_HAL_H_

#include <stdint.h>
#include "include/halcpp_base.h"
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wundefined-var-template"
#endif


namespace some_register_map_nm {


/*
* This register contains the part # and revision # for XYZ ASIC
*/
template<uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
class CHIP_ID_REG : public halcpp::RegRO<BASE, WIDTH, PARENT_TYPE> {
public:
    using TYPE = CHIP_ID_REG<BASE, WIDTH, PARENT_TYPE>;

    static halcpp::FieldRO<0, 3, TYPE> rev_num;
    static halcpp::FieldRO<4, 31, TYPE> part_num;

};



/*
* Toggle the peripheral enable on write
*/
template<uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
class ENABLE : public halcpp::RegWO<BASE, WIDTH, PARENT_TYPE> {
public:
    using TYPE = ENABLE<BASE, WIDTH, PARENT_TYPE>;

    static halcpp::FieldWO<0, 0, TYPE> enable;

    using halcpp::RegWO<BASE, WIDTH, PARENT_TYPE>::operator=;

};



}

/*
* This address map contains some example registers to show
* how RDL can be utilized in various situations.
*/
template <uint32_t BASE, typename PARENT_TYPE=void>
class SOME_REGISTER_MAP_HAL : public AddrmapNode<BASE, PARENT_TYPE> {
public:
    using TYPE = SOME_REGISTER_MAP_HAL<BASE, PARENT_TYPE>;

    static some_register_map_nm::CHIP_ID_REG<0x0, 32, TYPE> chip_id_reg;
    static some_register_map_nm::ENABLE<0x4, 1, TYPE> enable;


};

#endif