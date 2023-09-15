#include <assert.h>
#include <stdio.h>

#include "basic.h"

int main() {
    printf("checking SOME_REGISTER_MAP_CHIP_ID_REG is at address 0\n");
    assert(SOME_REGISTER_MAP_CHIP_ID_REG_ADDRESS==0U);
    printf("checking SOME_REGISTER_MAP_ENABLE is at address 4\n");
    assert(SOME_REGISTER_MAP_ENABLE_ADDRESS==4U);
}