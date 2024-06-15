// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/15 18:42
// Last Modified : 2024/06/15 23:32
// File Name     : dual_port_ram.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/06/15   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module dual_port_ram
#(
    parameter ADDRESS_WRITE_IN = 5,
    parameter ADDRESS_WRITE_OUT = 7,
    parameter DATA_WRITE_IN = 64,
    parameter DATA_WRITE_OUT = 16
)
(
    input CLK_WR, // write clk
    input WR_EN, // write enable
    input [ADDRESS_WRITE_IN-1:0] ADDR_WR, // write address
    input [DATA_WRITE_IN-1:0] D, // write data
    input CLK_RD, // read clk
    input RD_EN, // read enable
    input [ADDRESS_WRITE_OUT-1:0] ADDR_RD, // read address
    output reg [DATA_WRITE_OUT-1:0] Q //read data
);

    // output width large than input width, obtain extend factor and corresponding bits
    parameter EXTENT = DATA_WRITE_OUT/DATA_WRITE_IN;
    parameter EXTENT_BIT = ADDRESS_WRITE_IN - ADDRESS_WRITE_OUT > 0 ? ADDRESS_WRITE_IN - ADDRESS_WRITE_OUT : 'b1;
    // input width large than output width, obtain shrink factor and corresponding bits
    parameter SHRINK = DATA_WRITE_IN/DATA_WRITE_OUT;
    parameter SHRINK_BIT = ADDRESS_WRITE_OUT - ADDRESS_WRITE_IN > 0 ? ADDRESS_WRITE_OUT - ADDRESS_WRITE_IN : 'b1;

    genvar i;
    generate
        // data width extend(address width shrink)
        if (DATA_WRITE_OUT >= DATA_WRITE_IN) begin
            // write logic, once every cycle
            reg [DATA_WRITE_IN-1:0] mem [(ADDRESS_WRITE_IN<<1)-1:0];
            always @ (posedge CLK_WR) begin
                if (WR_EN) begin
                    mem[ADDR_WR] <= D;
                end
            end

            // read logic, four times every cycle
            for (i=0; i<EXTENT; i=i+1) begin
                always @ (CLK_RD) begin
                    if (RD_EN) begin
                        Q[(i+1)*DATA_WRITE_IN-1:i*DATA_WRITE_IN] <= mem[(ADDR_RD*EXTENT)+i];
                    end
                end
            end
        end

        // data width shrink(address width extend)
