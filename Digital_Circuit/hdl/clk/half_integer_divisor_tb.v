// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/08 22:53
// Last Modified : 2024/07/08 22:57
// File Name     : half_integer_divisor_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/07/08   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module half_integer_divisor_tb;

    reg rstn;
    reg clk100mhz;
    wire clk_div3p5;

    always #5 clk100mhz = ~clk100mhz;

    initial begin
        rstn = 1'b0;
        clk100mhz = 1'b0;
        #11;
        rstn = 1'b1;
    end

    half_integer_divisor u_half_integer_divisor
    (
        .rstn(rstn),
        .clk(clk100mhz),
        .clk_div3p5(clk_div3p5)
    );

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

    initial begin
        $fsdbDumpfile("half_integer_divisor.fsdb");
        $fsdbDumpvars(0, half_integer_divisor_tb);
    end

endmodule
