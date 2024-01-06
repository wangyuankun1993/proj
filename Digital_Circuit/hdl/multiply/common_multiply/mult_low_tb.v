// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/01/06 16:17
// Last Modified : 2024/01/06 17:23
// File Name     : mult_low_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/01/06   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module mult_low_tb;
    parameter N = 8;
    parameter M = 4;
    reg clk, rst_n;

    // clock
    always begin
        clk = 0; #5;
        clk = 1; #5;
    end

    // reset
    initial begin
        rst_n = 1'b0;
        #8; rst_n = 1'b1;
    end

    // no pipeline
    reg data_rdy_low;
    reg [N-1:0] mult1_low;
    reg [M-1:0] mult2_low;
    wire [M+N-1:0] result_low;
    wire result_rdy_low;

    // task cycle stimulus
    task mult_data_in;
        input [M+N-1:0] mult1_task, mult2_task;
        begin
            wait(!mult_low_tb.u_mult_low.result_rdy); // not output state
            @(negedge clk);
            data_rdy_low = 1'b1;
            mult1_low = mult1_task;
            mult2_low = mult2_task;
            @(negedge clk);
            data_rdy_low = 1'b0;
            wait(mult_low_tb.u_mult_low.result_rdy); // test the output state
        end
    endtask

    // driver
    initial begin
        #55;
        mult_data_in(25, 5);
        mult_data_in(16, 10);
        mult_data_in(10, 4);
        mult_data_in(15, 7);
        mult_data_in(215, 9);
    end

    mult_low #(.N(N), .M(M)) u_mult_low
    (
        .clk(clk),
        .rst_n(rst_n),
        .data_rdy(data_rdy_low),
        .mult1(mult1_low),
        .mult2(mult2_low),
        .result_rdy(result_rdy_low),
        .result(result_low)
    );

    initial begin
        $fsdbDumpfile("mult_low.fsdb");
        $fsdbDumpvars(0, mult_low_tb);
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
