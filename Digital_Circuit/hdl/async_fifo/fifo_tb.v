// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/23 14:14
// Last Modified : 2024/06/23 14:49
// File Name     : fifo_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/06/23   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps
`define SMALL2BIG

module fifo_tb;

`ifdef SMALL2BIG
    reg rstn;
    reg clk_slow, clk_fast;
    reg [3:0] din;
    reg din_en;
    wire [15:0] dout;
    wire dout_en;

    // reset
    initial begin
        clk_slow = 1'b0;
        clk_fast = 1'b0;
        rstn = 1'b0;
        #50 rstn = 1'b1;
    end

    parameter CYCLE_WR = 40;
    always #(CYCLE_WR/2/4) clk_slow = ~clk_slow;
    always #(CYCLE_WR/2-1) clk_fast = ~clk_fast;

    // data generate
    initial begin
        din = 16'h4321;
        din_en = 1'b0;
        wait(rstn);
        // test full, prog_full, empty
        force fifo_tb.u_fifo_s2b.u_fifo_small2big.ren = 1'b0;
        repeat(32) begin
            @(negedge clk_fast);
            din_en = 1'b1;
            din = {$random()} % 16;
        end
        @(negedge clk_fast) din_en = 1'b0;

        // test data read/write
        #500;
        rstn = 1'b0;
        #10 rstn = 1'b1;
        release fifo_tb.u_fifo_s2b.u_fifo_small2big.ren;
        repeat(100) begin
            @(negedge clk_fast);
            din_en = 1'b1;
            din = {$random()} % 16;
        end

        // stop read and test empty, full, prog_full
        force fifo_tb.u_fifo_s2b.u_fifo_small2big.ren = 1'b0;
        repeat(18) begin
            @(negedge clk_fast);
            din_en = 1'b1;
            din = {$random()} % 16;
        end
    end

    fifo_small2big u_fifo_small2big
    (
        .rstn(rstn),
        .din(din),
        .din_clk(clk_fast),
        .din_en(din_en),

        .dout(dout),
        .dout_clk(clk_slow),
        .dout_en(dout_en)
    );

`else
`endif

    initial begin
        forever begin
            #100;
            if($time >= 5000) $finish;
        end
    end

    initial begin
        $fsdbDumpfile("fifo.fsdb");
        $fsdbDumpvars(0, fifo_tb);
    end

endmodule
