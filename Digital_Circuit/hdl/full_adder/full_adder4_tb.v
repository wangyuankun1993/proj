// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/03 22:32
// Last Modified : 2023/09/03 22:45
// File Name     : full_adder4_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/03   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module full_adder4_tb;

    reg [3:0] a;
    reg [3:0] b;

    wire [3:0] so;
    wire co;

    initial begin
        a = 4'd5;
        b = 4'd2;
        #10;
        a = 4'd10;
        b = 4'd8;
    end

    full_adder4 u_full_adder4(
        .a(a),
        .b(b),
        .c(1'b0),
        .so(so),
        .co(co)
    );

    initial begin
        $fsdbDumpfile("full_adder4.fsdb");
        $fsdbDumpvars(0, full_adder4_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000)
                $finish;
        end
    end

endmodule
