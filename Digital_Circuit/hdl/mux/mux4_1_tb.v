// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/08/24 00:26
// Last Modified : 2023/08/24 00:34
// File Name     : mux4_1_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/08/24   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module mux4_1_tb;
    reg [1:0] sel;
    wire [1:0] sout;

    initial begin
        sel = 0;
        #10 sel = 2'b11;
        #10 sel = 2'b01;
        #10 sel = 2'b00;
        #10 sel = 2'b10;
    end

    mux4_1 u_mux4_1(
        .sel(sel),
        .p0(2'b00),
        .p1(2'b01),
        .p2(2'b10),
        .p3(2'b11),
        .sout(sout)
    );

    initial begin
        $fsdbDumpfile("mux4_1.fsdb");
        $fsdbDumpvars(0, mux4_1_tb);
    end

    always begin
        #100;
        if ($time >= 1000) $finish;
    end

endmodule
