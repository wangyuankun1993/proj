// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/10/10 23:49
// Last Modified : 2023/10/15 11:47
// File Name     : vending_machine_moore_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/10/10   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module vending_machine_moore_tb;
    reg clk;
    reg rstn;
    reg [1:0] coin;
    wire [1:0] change;
    wire sell;

    // clock generating
    parameter CYCLE_100MHz = 10;
    always begin
        clk = 0; #(CYCLE_100MHz/2);
        clk = 1; #(CYCLE_100MHz/2);
    end

    // motivation generating
    reg [9:0] buy_oper; // store state of the buy operation
    initial begin
        buy_oper = 10'b0;
        coin = 2'b0;
        rstn = 1'b0;
        #8 rstn = 1'b1;
        @(negedge clk);

        // case(1) 0.5 -> 0.5 -> 0.5 -> 0.5
        #16;
        buy_oper = 10'b00_0101_0101;
        repeat(5) begin
            @(negedge clk);
            coin = buy_oper[1:0];
            buy_oper = buy_oper >> 2;
        end

        // case(2) 1 -> 0.5 -> 1, taking change
        #16;
        buy_oper = 10'b00_0010_0110;
        repeat(5) begin
            @(negedge clk);
            coin = buy_oper[1:0];
            buy_oper = buy_oper >> 2;
        end

        // case(3) 0.5 -> 1 -> 0.5
        #16;
        buy_oper = 10'b00_0001_1001;
        repeat(5) begin
            @(negedge clk);
            coin = buy_oper[1:0];
            buy_oper = buy_oper >> 2;
        end

        // case(4) 0.5 -> 0.5 -> 0.5 -> 1, taking change
        buy_oper = 10'b00_1001_0101;
        repeat(5) begin
            @(negedge clk)
            coin = buy_oper[1:0];
            buy_oper = buy_oper >> 2;
        end
    end

    // mealy state with 3-stage
    vending_machine_moore u_vending_machine_moore(
        .clk(clk),
        .rstn(rstn),
        .coin(coin),
        .change(change),
        .sell(sell)
    );

    initial begin
        $fsdbDumpfile("vending_machine_moore.fsdb");
        $fsdbDumpvars(0, vending_machine_moore_tb);
    end

    always begin
        #100;
        if ($time >= 10000) begin
            $finish;
        end
    end

endmodule
