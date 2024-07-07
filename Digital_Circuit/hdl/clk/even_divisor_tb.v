// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/06 19:04
// Last Modified : 2024/07/06 19:13
// File Name     : even_divisor_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/07/06   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module even_divisor_tb;

    reg rstn;
    reg clk100mhz;
    wire clk_div2;
    wire clk_div4;
    wire clk_div10;

    always #5 clk100mhz = ~clk100mhz;

    initial begin
        clk100mhz = 1'b0;
        rstn = 1'b0;
        #11;
        rstn = 1'b1;
    end

    even_divisor u_even_divisor
    (
        .rstn(rstn),
        .clk(clk100mhz),
        .clk_div2(clk_div2),
        .clk_div4(clk_div4),
        .clk_div10(clk_div10)
    );

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

    initial begin
        $fsdbDumpfile("even_divisor.fsdb");
        $fsdbDumpvars(0, even_divisor_tb);
    end

endmodule
