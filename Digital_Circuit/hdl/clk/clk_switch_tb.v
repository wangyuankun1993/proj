// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/08/04 22:20
// Last Modified : 2024/08/04 22:46
// File Name     : clk_switch_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/08/04   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module clk_switch_tb;

    reg clk_100mhz, clk_200mhz;
    reg rstn;
    reg sel;
    wire clk_out;

    always #(2.5) clk_200mhz = ~clk_200mhz;
    always @ (posedge clk_200mhz) clk_100mhz = #1 ~clk_100mhz;

    initial begin
        clk_100mhz = 1'b0;
        clk_200mhz = 1'b0;
        rstn = 1'b0;
        sel = 1'b1;
        #11 rstn = 1'b1;
        #36.2 sel = ~sel;
        #119.7 sel = ~sel;
    end

    clk_switch u_clk_switch
    (
        .rstn(rstn),
        .clk1(clk_100mhz),
        .clk2(clk_200mhz),
        .sel_clk1(sel),
        .clk_out(clk_out)
    );

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

    initial begin
        $fsdbDumpfile("clk_switch.fsdb");
        $fsdbDumpvars(0, clk_switch_tb);
    end

endmodule
