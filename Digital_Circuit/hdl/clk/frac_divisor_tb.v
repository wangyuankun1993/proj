// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/27 16:54
// Last Modified : 2024/07/28 13:18
// File Name     : frac_divisor_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/07/27   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module frac_divisor_tb;

    reg rstn;
    reg clk100mhz;
    wire clk_frac;

    always #5 clk100mhz = ~clk100mhz;

    initial begin
        rstn = 1'b0;
        clk100mhz = 1'b0;
        #11;
        rstn = 1'b1;
    end

    frac_divisor u_frac_divisor
    (
        .rstn(rstn),
        .clk(clk100mhz),
        .clk_frac(clk_frac)
    );

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

    initial begin
        $fsdbDumpfile("frac_divisor.fsdb");
        $fsdbDumpvars(0, frac_divisor_tb);
    end

endmodule
