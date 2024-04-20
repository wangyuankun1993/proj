// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/04/20 12:10
// Last Modified : 2024/04/20 12:20
// File Name     : and4_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/04/20   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module and4_tb;

    reg a, b, c, d;
    wire out;

    initial begin
        a = 1;
        b = 1;
        c = 1;
        d = 1;
        #0.5 a = 0;
        #0.5 a = 1;
        #0.5 b = 0;
        #0.5 b = 1;
        #0.5 c = 0;
        #0.5 c = 1;
        #0.5 d = 0;
        #0.5 d = 1;
    end

    and4 u_and4
    (
        .out(out),
        .a(a),
        .b(b),
        .c(c),
        .d(d)
    );

    initial begin
        $fsdbDumpfile("and4.fsdb");
        $fsdbDumpvars(0, and4_tb);
    end

    initial begin
        forever begin
            #100
            if ($time >= 1000)
                $finish;
        end
    end

endmodule
