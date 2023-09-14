// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/14 00:44
// Last Modified : 2023/09/15 00:05
// File Name     : xor_oper_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/14   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module xor_oper_tb;

    reg clk, rstn;

    initial begin
        rstn = 1'b0;
        #8 rstn = 1'b1;
        forever begin
            clk = 1'b0; #5;
            clk = 1'b1; #5;
        end
    end

    reg [3:0] a, b;
    wire [3:0] co;

    initial begin
        a = 4'b0;
        b = 4'b0;
        sig_input(4'b1111, 4'b1001, a, b);
        sig_input(4'b0110, 4'b1001, a, b);
        sig_input(4'b1000, 4'b1001, a, b);
    end

    task sig_input;
        input [3:0] a;
        input [3:0] b;
        output [3:0] ao;
        output [3:0] bo;
        @(posedge clk);
        ao = a;
        bo = b;
    endtask

    xor_oper u_xor_oper(
        .clk(clk),
        .rstn(rstn),
        .a(a),
        .b(b),
        .co(co)
    );

    initial begin
        $fsdbDumpfile("xor_oper.fsdb");
        $fsdbDumpvars(0, xor_oper_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000)
                $finish;
        end
    end

endmodule
