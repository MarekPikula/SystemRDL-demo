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
--! @date 2021-04-07
--! @author Michael Büchler <michael.buechler@desy.de>
--! @author Lukasz Butkowski <lukasz.butkowski@desy.de>
------------------------------------------------------------------------------
--! @brief
--! Top component of DesyRDL address space decoder for {node.type_name}
------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_some_register_map.all;

entity some_register_map is
  port (
    pi_clock : in std_logic;
    pi_reset : in std_logic;
    -- TOP subordinate memory mapped interface
    pi_s_reset : in std_logic := '0';
    pi_s_top   : in  t_some_register_map_m2s;
    po_s_top   : out t_some_register_map_s2m;
    -- to logic interface
    pi_addrmap : in  t_addrmap_some_register_map_in;
    po_addrmap : out t_addrmap_some_register_map_out
  );
end entity some_register_map;

architecture arch of some_register_map is

  type t_data_out is array (natural range<>) of std_logic_vector(C_DATA_WIDTH-1 downto 0) ;

  --
  signal reg_data_out_vect : t_data_out(2-1 downto 0);
  signal reg_rd_stb   : std_logic_vector(2-1 downto 0);
  signal reg_wr_stb   : std_logic_vector(2-1 downto 0);
  signal reg_data_in  : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  signal reg_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
  --

begin

  ins_decoder_axi4l : entity work.some_register_map_decoder_axi4l
  generic map (
    g_addr_width    => C_ADDR_WIDTH,
    g_data_width    => C_DATA_WIDTH
  )
  port map (
    pi_clock      => pi_clock,
    pi_reset      => pi_reset,

    --
    po_reg_rd_stb => reg_rd_stb,
    po_reg_wr_stb => reg_wr_stb,
    po_reg_data   => reg_data_in,
    pi_reg_data   => reg_data_out,
    --
    --
    --
    --
    pi_s_reset  => pi_s_reset,
    pi_s_top    => pi_s_top,
    po_s_top    => po_s_top
  );
  --
  prs_reg_rd_mux: process(pi_clock)
  begin
    if rising_edge(pi_clock) then
      for idx in 0 to 2-1 loop
        if reg_rd_stb(idx) = '1' then
          reg_data_out <= reg_data_out_vect(idx);
        end if;
      end loop;
    end if;
  end process prs_reg_rd_mux;
  --
  --
  --

  -- ===========================================================================
  -- generated registers instances
  -- ---------------------------------------------------------------------------
  -- reg name: chip_id_reg  reg type: chip_id_reg
  -- ---------------------------------------------------------------------------
  blk_chip_id_reg : block
  begin  --
    inst_chip_id_reg: entity work.some_register_map_chip_id_reg
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(0),
        pi_decoder_wr_stb => reg_wr_stb(0),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(0),

        pi_reg  => pi_addrmap.chip_id_reg,
        po_reg  => po_addrmap.chip_id_reg
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: enable  reg type: enable
  -- ---------------------------------------------------------------------------
  blk_enable : block
  begin  --
    inst_enable: entity work.some_register_map_enable
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(1),
        pi_decoder_wr_stb => reg_wr_stb(1),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(1),

        pi_reg  => pi_addrmap.enable,
        po_reg  => po_addrmap.enable
      ); --
  end block; --

  -- ===========================================================================
  -- generated registers instances in regfiles 

  -- ===========================================================================
  -- Generated Meme Instances
  --
  -- ---------------------------------------------------------------------------

  -- ===========================================================================
  -- External Busses

end architecture;
