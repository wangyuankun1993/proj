// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : YuankunWang
// Email         : yuankun.wang@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/01/02 18:35
// Last Modified : 2023/01/02 19:42
// File Name     : counter10_tb.v
// Description   :
//         
// Copyright (c) 2023 Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/01/02   YuankunWang     1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps
    //==================(1)==================
    // signals declaration
module counter10_tb;
    reg rstn;
    reg clk;
    wire [3:0] cnt;
    wire cout;

    //==================(2)==================
    // clock generating
    real CYCLE_200MHz = 5;
    always begin
        clk = 0; #(CYCLE_200MHz);
        clk = 1; #(CYCLE_200MHz);
    end

    //==================(3)==================
    // reset generating
    initial begin
        rstn = 1'b0;
        #12; rstn = 1'b1;
    end

    //==================(4)==================
    // module instantiation
    counter10 u_counter10
    (
        .clk(clk),
        .rstn(rstn),
        .cnt(cnt),
        .cout(cout)
    );

    //==================(5)==================
    // dump wave
    initial begin
        $fsdbDumpfile("counter10.fsdb");
        $fsdbDumpvars(0, counter10_tb);
    end

    //==================(6)==================
    // simulation finish
    always begin
        #100;
        if ($time >= 500) begin
            $display("-------------------------");
            $display("Data process is OK!!!");
            $display("-------------------------");
            #1;
            $finish;
        end
    end
endmodule
