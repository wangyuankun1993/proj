// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/07 15:05
// Last Modified : 2024/07/07 15:06
// File Name     : odd_divisor_and_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/07/07   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module odd_divisor_and_tb;

    reg rstn;
    reg clk100mhz;
    wire clk_div9;

    always #5 clk100mhz = ~clk100mhz;

    initial begin
        rstn = 1'b0;
        clk100mhz = 1'b0;
        #11;
        rstn = 1'b1;
    end

    odd_divisor_and u_odd_divisor_and
    (
        .rstn(rstn),
        .clk(clk100mhz),
        .clk_div9(clk_div9)
    );

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

    initial begin
        $fsdbDumpfile("odd_divisor_and.fsdb");
        $fsdbDumpvars(0, odd_divisor_and_tb);
    end

endmodule
