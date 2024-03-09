// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/03/09 17:12
// Last Modified : 2024/03/09 23:26
// File Name     : divider_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/03/09   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module divider_tb;

    parameter N = 5;
    parameter M = 3;
    reg clk;
    reg rst_n;
    reg data_enable;
    reg [N-1:0] dividend;
    reg [M-1:0] divisor;

    wire result_ready;
    wire [N-1:0] merchant;
    wire [M-1:0] remainder;

    // clock
    always begin
        clk = 1'b0; #5;
        clk = 1'b1; #5;
    end

    // driver
    initial begin
        rst_n = 1'b0;
        #8;
        rst_n = 1'b1;
        #55;
        @(negedge clk);
        data_enable = 1'b1;
        dividend = 25; divisor = 5; #10;
        dividend = 16; divisor = 3; #10
        dividend = 10; divisor = 4; #10;
        dividend = 15; divisor = 1;
        repeat(32) #10 dividend = dividend + 1;
        divisor = 7;
        repeat(32) #10 dividend = dividend + 1;
        divisor = 5;
        repeat(32) #10 dividend = dividend + 1;
        divisor = 4;
        repeat(32) #10 dividend = dividend + 1;
        divisor = 6;
        repeat(32) #10 dividend = dividend + 1;
    end

    // delay input for result comparison in the same period and complete-check
    reg [N-1:0] dividend_ref [N-1:0];
    reg [M-1:0] divisor_ref [N-1:0];
    always @ (posedge clk) begin
        dividend_ref[0] <= dividend;
        divisor_ref[0] <= divisor;
    end

    genvar i;
    generate
        for(i=1;i<=N-1;i=i+1) begin
            always @ (posedge clk) begin
                dividend_ref[i] <= dividend_ref[i-1];
                divisor[i] <= divisor[i-1];
            end
        end
    endgenerate

    // self-check
    reg error_flag;
    always @ (posedge clk) begin
        #1;
        if (merchant * divisor_ref[N-1] + remainder != dividend_ref[N-1] && result_ready) begin
            error_flag <= 1'b1;
        end
        else begin
            error_flag <= 1'b0;
        end
    end

    // module instantiation
    divider_man #(.N(N), .M(M)) u_divider_man
    (
        .clk(clk),
        .rst_n(rst_n),
        .data_enable(data_enable),
        .dividend(dividend),
        .divisor(divisor),
        .result_ready(result_ready),
        .merchant(merchant),
        .remainder(remainder)
    );

    initial begin
        $fsdbDumpfile("divider.fsdb");
        $fsdbDumpvars(0, divider_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

endmodule
