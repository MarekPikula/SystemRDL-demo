------------------------------------------------------------------------------
--          ____  _____________  __                                         --
--         / __ \/ ____/ ___/\ \/ /                 _   _   _               --
--        / / / / __/  \__ \  \  /                 / \ / \ / \              --
--       / /_/ / /___ ___/ /  / /               = ( M | S | K )=            --
--      /_____/_____//____/  /_/                   \_/ \_/ \_/              --
--                                                                          --
------------------------------------------------------------------------------
--! @copyright Copyright 2021-2022 DESY
--! SPDX-License-Identifier: Apache-2.0
------------------------------------------------------------------------------
--! @date 2021-10-01
--! @author Michael Büchler <michael.buechler@desy.de>
--! @author Lukasz Butkowski <lukasz.butkowski@desy.de>
------------------------------------------------------------------------------
--! @brief
--! VHDL package of DesyRDL for address space decoder for {node.orig_type_name}
------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

-- library desy;
-- use desy.common_axi.all;

package pkg_some_register_map is

  -----------------------------------------------
  -- per addrmap / module
  -----------------------------------------------
  constant C_ADDR_WIDTH : integer := 3;
  constant C_DATA_WIDTH : integer := 32;

  -- ===========================================================================
  -- ---------------------------------------------------------------------------
  -- registers
  -- ---------------------------------------------------------------------------

  -- ===========================================================================
  -- REGISTERS interface
  -- ---------------------------------------------------------------------------
  -- register type: chip_id_reg
  -----------------------------------------------
  type t_field_signals_chip_id_reg_rev_num_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_chip_id_reg_rev_num_out is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record; --
  type t_field_signals_chip_id_reg_part_num_in is record
    data : std_logic_vector(28-1 downto 0); --
  end record;

  type t_field_signals_chip_id_reg_part_num_out is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_chip_id_reg_in is record--
    rev_num : t_field_signals_chip_id_reg_rev_num_in; --
    part_num : t_field_signals_chip_id_reg_part_num_in; --
  end record;
  type t_reg_chip_id_reg_out is record--
    rev_num : t_field_signals_chip_id_reg_rev_num_out; --
    part_num : t_field_signals_chip_id_reg_part_num_out; --
  end record;
  type t_reg_chip_id_reg_2d_in is array (integer range <>) of t_reg_chip_id_reg_in;
  type t_reg_chip_id_reg_2d_out is array (integer range <>) of t_reg_chip_id_reg_out;
  type t_reg_chip_id_reg_3d_in is array (integer range <>, integer range <>) of t_reg_chip_id_reg_in;
  type t_reg_chip_id_reg_3d_out is array (integer range <>, integer range <>) of t_reg_chip_id_reg_out;
  -----------------------------------------------
  -- register type: enable
  -----------------------------------------------
  type t_field_signals_enable_enable_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_enable_enable_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_enable_in is record--
    enable : t_field_signals_enable_enable_in; --
  end record;
  type t_reg_enable_out is record--
    enable : t_field_signals_enable_enable_out; --
  end record;
  type t_reg_enable_2d_in is array (integer range <>) of t_reg_enable_in;
  type t_reg_enable_2d_out is array (integer range <>) of t_reg_enable_out;
  type t_reg_enable_3d_in is array (integer range <>, integer range <>) of t_reg_enable_in;
  type t_reg_enable_3d_out is array (integer range <>, integer range <>) of t_reg_enable_out;
  -----------------------------------------------

  ------------------------------------------------------------------------------
  -- Register types in regfiles --

  -- ===========================================================================
  -- REGFILE interface
  -- -----------------------------------------------------------------------------

  -- ===========================================================================
  -- MEMORIES interface
  -- ---------------------------------------------------------------------------

  -- ===========================================================================
  -- some_register_map : Top module address map interface
  -- ---------------------------------------------------------------------------
  type t_addrmap_some_register_map_in is record
    --
    chip_id_reg : t_reg_chip_id_reg_in; --
    enable : t_reg_enable_in; --
    --
    --
    --
  end record;

  type t_addrmap_some_register_map_out is record
    --
    chip_id_reg : t_reg_chip_id_reg_out; --
    enable : t_reg_enable_out; --
    --
    --
    --
  end record;

  -- ===========================================================================
  -- top level component declaration
  -- must come after defining the interfaces
  -- ---------------------------------------------------------------------------
  subtype t_some_register_map_m2s is t_axi4l_m2s;
  subtype t_some_register_map_s2m is t_axi4l_s2m;

  component some_register_map is
      port (
        pi_clock : in std_logic;
        pi_reset : in std_logic;
        -- TOP subordinate memory mapped interface
        pi_s_top  : in  t_some_register_map_m2s;
        po_s_top  : out t_some_register_map_s2m;
        -- to logic interface
        pi_addrmap : in  t_addrmap_some_register_map_in;
        po_addrmap : out t_addrmap_some_register_map_out
      );
  end component some_register_map;

end package pkg_some_register_map;
--------------------------------------------------------------------------------
package body pkg_some_register_map is
end package body;

--==============================================================================


--------------------------------------------------------------------------------
-- Register types directly in addmap
--------------------------------------------------------------------------------
--
-- register type: chip_id_reg
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_some_register_map.all;

entity some_register_map_chip_id_reg is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_chip_id_reg_in ;
    po_reg  : out t_reg_chip_id_reg_out
  );
end entity some_register_map_chip_id_reg;

architecture rtl of some_register_map_chip_id_reg is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------WIRE
  rev_num_wire : block--
  begin
    --
    data_out(3 downto 0) <= std_logic_vector(to_signed(1,4)); --
    --no signal to read by HW
    po_reg.rev_num.data <= (others => '0'); --
  end block; ----WIRE
  part_num_wire : block--
  begin
    --
    data_out(31 downto 4) <= pi_reg.part_num.data(28-1 downto 0); --
    --no signal to read by HW
    po_reg.part_num.data <= (others => '0'); --
  end block; --
end rtl;
-----------------------------------------------
-- register type: enable
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_some_register_map.all;

entity some_register_map_enable is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_enable_in ;
    po_reg  : out t_reg_enable_out
  );
end entity some_register_map_enable;

architecture rtl of some_register_map_enable is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --
  data_out(C_DATA_WIDTH-1 downto 1) <= (others => '0'); --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------STORAGE
  enable_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0);
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(0 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.enable.data <= l_field_reg; --
    data_out(0 downto 0) <= l_field_reg;

  end block enable_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------

--------------------------------------------------------------------------------
-- Register types in regfiles
--------------------------------------------------------------------------------
--