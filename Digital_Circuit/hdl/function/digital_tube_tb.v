// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/09 00:42
// Last Modified : 2023/09/09 00:53
// File Name     : digital_tube_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/09   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module digital_tube_tb;

    reg clk;
    reg rstn;
    reg en;
    reg [3:0] single_digit;
    reg [3:0] ten_digit;
    reg [3:0] hundred_digit;
    reg [3:0] kilo_digit;
    wire [3:0] csn;
    wire [6:0] abcdefg;

    digital_tube u_digital_tube(
        .clk(clk),
        .rstn(rstn),
        .en(en),
        .single_digit(single_digit),
        .ten_digit(ten_digit),
        .hundred_digit(hundred_digit),
        .kilo_digit(kilo_digit),
        .csn(csn),
        .abcdefg(abcdefg)
    );

    always begin
        clk = 1'b0; #5;
        clk = 1'b1; #5;
    end

    initial begin
        rstn = 1'b0;
        en = 1'b0;
        single_digit = 4'd1;
        ten_digit = 4'd2;
        hundred_digit = 4'd3;
        kilo_digit = 4'd4;
        #5;
        rstn = 1'b1;
        forever begin
            en = 1'b1;
            repeat (5) @(negedge clk);
            single_digit = single_digit + 4'd5;
            ten_digit = ten_digit + 4'd5;
            hundred_digit = hundred_digit + 4'd5;
            kilo_digit = kilo_digit + 4'd5;
        end
    end

    initial begin
        $fsdbDumpfile("digital_tube.fsdb");
        $fsdbDumpvars(0, digital_tube_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000)
                $finish;
        end
    end

endmodule
