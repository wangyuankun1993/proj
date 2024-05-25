// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/05/25 13:06
// Last Modified : 2024/05/25 15:06
// File Name     : test.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/05/25   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps
`define LOGIC_BUF

module test;

    reg [3:0] a;
    reg [3:0] b;
    reg clk;
    wire [3:0] so;
    wire co;

    parameter CYCLE_10NS = 10;
    initial begin
        clk = 0;
        #111;
        forever begin
            #(CYCLE_10NS/2) clk = ~clk;
        end
    end

    reg slow_flag = 0;
    always @ (posedge clk) begin
`ifdef LOGIC_BUF
        slow_flag <= ~slow_flag;
`else
        slow_flag <= 1'b1;
`endif
    end

    reg [7:0] num = 0;
    always @ (posedge clk) begin
        if (slow_flag)
            num[3:0] <= num[3:0] + 1;
    end

    // num * 8 + num * 4
    wire [7:0] adder1;
    full_adder8 u_full_adder8_1
    (
        .a(num<<3),
        .b(num<<2),
        .c(1'b0),
        .so(adder1),
        .co()
    );
    
    // num * 2 + num
    wire [7:0] adder2;
    full_adder8 u_full_adder8_2
    (
        .a(num<<1),
        .b(num),
        .c(1'b0),
        .so(adder2),
        .co()
    );

    // ---------for better time------------
    reg [7:0] adder1_r, adder2_r;
    dff8 u_dff8_1
    (
        .d(adder1),
        .clk(clk),
        .q(adder1_r)
    );
    dff8 u_dff8_2
    (
        .d(adder2),
        .clk(clk),
        .q(adder2_r)
    );

`ifdef LOGIC_BUF
    wire [7:0] adder1_t = adder1_r;
    wire [7:0] adder2_t = adder2_r;
`else
    wire [7:0] adder1_t = adder1;
    wire [7:0] adder2_t = adder2;
`endif

    // num * 15
    wire [7:0] adder3;
    full_adder8 u_full_adder8_3
    (
        .a(adder1_t),
        .b(adder2_t),
        .c(1'b0),
        .so(adder3),
        .co()
    );

    reg [7:0] res_mul15;
    dff8 u_dff8
    (
        .d(adder3),
        .clk(clk),
        .q(res_mul15)
    );

    initial begin
        $fsdbDumpfile("test.fsdb");
        $fsdbDumpvars(0, test);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000) $finish;
        end
    end

endmodule
