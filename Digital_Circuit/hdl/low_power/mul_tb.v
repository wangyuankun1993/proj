// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/08/17 18:19
// Last Modified : 2024/08/17 18:38
// File Name     : mul_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/08/17   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module mul_tb;

    reg rstn;
    // mul1_hs
    reg hs_clk;
    reg hs_en;
    reg [3:0] hs_mul1;
    reg [3:0] hs_mul2;
    wire hs_dout_en;
    wire [8:0] hs_dout;
    // mul2_ls
    reg ls_clk = 0;
    reg ls_en;
    reg [3:0] ls_mul1;
    reg [3:0] ls_mul2;
    reg [3:0] ls_mul3;
    reg [3:0] ls_mul4;
    wire ls_dout_en;
    wire [8:0] ls_dout;

    // clock generating
    real CYCLE_200MHz = 5;
    always begin
        hs_clk = 0; #(CYCLE_200MHz/2);
        hs_clk = 1; #(CYCLE_200MHz/2);
    end

    always begin
        @(posedge hs_clk) ls_clk = ~ls_clk;
    end

    // reset generating
    initial begin
        rstn = 1'b0;
        #8 rstn = 1'b1;
    end

    initial begin
        hs_mul1 = 0;
        hs_mul2 = 16;
        hs_en = 0;
        #103;
        repeat(12) begin
            @(negedge hs_clk);
            hs_en = 1;
            hs_mul1 = hs_mul1 + 1;
            hs_mul2 = hs_mul2 - 1;
        end
        hs_en = 0;
    end

    initial begin
        ls_mul1 = 1;
        ls_mul2 = 15;
        ls_mul3 = 2;
        ls_mul4 = 14;
        ls_en = 0;
        #103;
        @(negedge ls_clk) ls_en = 1;
        repeat(5) begin
            @(negedge ls_clk);
            ls_mul1 = ls_mul1 + 2;
            ls_mul2 = ls_mul2 - 2;
            ls_mul3 = ls_mul3 + 2;
            ls_mul4 = ls_mul4 - 2;
        end
        ls_en = 0;
    end

    mul1_hs u_mul1_hs
    (
        .clk(hs_clk),
        .rstn(rstn),
        .en(hs_en),
        .mul1(hs_mul1),
        .mul2(hs_mul2),
        .dout(hs_dout),
        .dout_en(hs_dout_en)
    );

    mul2_ls u_mul2_ls
    (
        .clk(ls_clk),
        .rstn(rstn),
        .en(ls_en),
        .mul1(ls_mul1),
        .mul2(ls_mul2),
        .mul3(ls_mul3),
        .mul4(ls_mul4),
        .dout(ls_dout),
        .dout_en(ls_dout_en)
    );

    always begin
        #100;
        if ($time >= 1000) begin
            $finish;
        end
    end

    initial begin
        $fsdbDumpfile("low_power.fsdb");
        $fsdbDumpvars(0, mul_tb);
    end

endmodule
