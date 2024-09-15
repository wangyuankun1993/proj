// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/09/15 14:02
// Last Modified : 2024/09/15 16:42
// File Name     : clkgate_basic.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/09/15   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module clkgate_basic
(
    input clk,
    input clken,
    input rstn,
    input wr_en,
    input [3:0] addr,
    input [7:0] data,
    output [7:0] q
);

    // using latch
    reg en_latch;
    always @ (*) begin
        if (~clk) begin
            en_latch <= clken;
        end
    end
    wire clk_gate = clk & en_latch;

    ram
    #(4, 8)
    u1_ram16x8
    (
        .CLK(clk_gate),
        .A(addr),
        .D(data),
        .EN(clken),
        .WR(wr_en),
        .Q(q)
    );

endmodule
