// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/09/15 15:39
// Last Modified : 2024/09/15 16:13
// File Name     : clkgate_basic_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/09/15   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module clkgate_basic_tb;

    reg rstn;
    reg clk;
    reg clken;
    reg wr_en;
    reg [3:0] addr;
    reg [7:0] data;
    wire [7:0] q;

    initial begin
        rstn = 1'b0;
        #7 rstn = 1'b1;
    end

    always begin
        #50 clk = 1'b0;
        #50 clk = 1'b1;
    end

    initial begin
        clken = 1'b0;
        wr_en = 1'b0;
        addr = 4'h3;
        data = 8'h31;
        #53;
        // normal write and read
        clken = 1'b1;
        wr_en = 1'b1;
        repeat(9) begin
            @(negedge clk);
            data = data + 1'b1;
            addr = addr + 1'b1;
        end

        @(negedge clk);
        clken = 1'b0;
        wr_en = 1'b0;

        #211;
        addr = 4'h3;
        clken = 1'b1;
        repeat(9) begin
            @(negedge clk);
            addr = addr + 1'b1;
        end
        @(negedge clk);
        clken = 1'b0;

        // jitter at the end of read
        #985;
        addr = 4'h3;
        clken = 1'b1;
        repeat(9) begin
            @(negedge clk);
            addr = addr + 1'b1;
        end
        @(negedge clk);
        clken = 1'b0;
        #20 clken = 1'b1;
        #21 clken = 1'b0;
        #31 clken = 1'b1;
        #13 clken = 1'b0;
    end

    clkgate_basic u_clkgate_basic
    (
        .clk(clk),
        .clken(clken),
        .rstn(rstn),
        .wr_en(wr_en),
        .addr(addr),
        .data(data),
        .q(q)
    );

    always begin
        #100;
        if ($time >= 10000) begin
            #1;
            $finish;
        end
    end

    initial begin
        $fsdbDumpfile("clkgate_basic.fsdb");
        $fsdbDumpvars(0, clkgate_basic_tb);
    end

endmodule
