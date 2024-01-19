// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/01/18 08:40
// Last Modified : 2024/01/19 23:22
// File Name     : mult_man_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/01/18   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps
module mult_man_tb;

    parameter N=8;
    parameter M=4;

    reg clk, rst_n;
    reg data_ready;
    reg [N-1:0] mult1;
    reg [M-1:0] mult2;
    wire result_ready;
    wire [N+M-1:0] result;

    always begin
        clk = 0; #5;
        clk = 1; #5;
    end

    initial begin
        rst_n = 1'b0;
        #8; rst_n = 1'b1;
    end

    // driver
    initial begin
        #55;
        @(negedge clk);
        data_ready = 1'b1;
        mult1 = 25; mult2 = 5;
        #10; mult1 = 16; mult2 = 10;
        #10; mult1 = 10; mult2 = 4;
        #10; mult1 = 15; mult2 = 7;
        mult2 = 7; repeat(32) #10 mult1 = mult1 + 1;
        mult2 = 1; repeat(32) #10 mult1 = mult1 + 1;
        mult2 = 15; repeat(32) #10 mult1 = mult1 + 1;
        mult2 = 3; repeat(32) #10 mult1 = mult1 + 1;
        mult2 = 11; repeat(32) #10 mult1 = mult1 + 1;
        mult2 = 4; repeat(32) #10 mult1 = mult1 + 1;
        mult2 = 9; repeat(32) #10 mult1 = mult1 + 1;
    end

    // shift input data for check
    reg [N-1:0] mult1_ref [M-1:0];
    reg [M-1:0] mult2_ref [M-1:0];
    always @ (posedge clk) begin
        mult1_ref[0] <= mult1;
        mult2_ref[0] <= mult2;
    end

    genvar i;
    generate
        for (i=1; i<=M-1; i=i+1) begin
            always @ (posedge clk) begin
                mult1_ref[i] <= mult1_ref[i-1];
                mult2_ref[i] <= mult2_ref[i-1];
            end
        end
    endgenerate

    // self check
    reg error_flag;
    always @ (posedge clk) begin
        #1;
        if (mult1_ref[M-1] * mult2_ref[M-1] != result && result_ready) begin
            error_flag <= 1'b1;
        end
        else begin
            error_flag <= 1'b0;
        end
    end

    // module instantiation
    mult_man #(.N(N), .M(M)) u_mult_man
    (
        .clk(clk),
        .rst_n(rst_n),
        .data_ready(data_ready),
        .mult1(mult1),
        .mult2(mult2),
        .result_ready(result_ready),
        .result(result)
    );

    initial begin
        $fsdbDumpfile("mult_man.fsdb");
        $fsdbDumpvars(0, mult_man_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 10000) begin
                $finish;
            end
        end
    end

endmodule
