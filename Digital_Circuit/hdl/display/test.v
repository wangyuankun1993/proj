// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/09/16 14:56
// Last Modified : 2024/09/16 15:47
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
// 2024/09/16   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module test;

    reg clk;

    initial begin
        clk = 1'b0;
    end

    always #5 clk = ~clk;

    // $display
    reg [3:0] num;
    initial begin
        num = 4'b1;
        $display("This is a test.");
        $display("This is a test number: %b.", num);
        $display("This is a test number: ", num, "!!!");
    end

    // $write
    initial begin
        #4;
        $write("This is a test");
        $write("number: %b", num);
        $write("!!!\n");
    end

    // $strobe
    reg [3:0] a;
    initial begin
        a = 1'b1;
        #1;
        a <= a + 1;
        $display("$display excuting result: %d.", a);
        $strobe("$strobe excuting result: %d.", a);
        #1;
        $display();
        $display("$display excuting result: %d.", a);
        $strobe("$strobe excuting result: %d.", a);
    end

    integer i;
    initial begin
        #8;
        for(i=0; i<4; i=i+1) begin
            $display("Run times of $display: %d.", i);
            $strobe("Run times of $strobe: %d.", i);
        end
    end

    //$monitor
    reg [3:0] cnt;
    initial begin
        cnt = 4'b11;
        forever begin
            #5;
            if (cnt < 7) cnt = cnt + 1;
        end
    end

    initial begin
        $monitor("Counter change to value %d at time %t.", cnt, $time);
    end

    always begin
        #100;
        if ($time >= 10000) begin
            $finish;
        end
    end

endmodule
