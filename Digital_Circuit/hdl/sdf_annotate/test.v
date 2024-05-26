// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/05/26 18:34
// Last Modified : 2024/05/26 19:05
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
// 2024/05/26   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module test;

    wire and_out;
    reg in1, in2;
    reg clk;

    initial begin
        clk = 0;
        forever begin
            #5 clk = ~clk;
        end
    end

    initial begin
        in1 = 0; in2 = 0;
        #32;
        in1 = 1; in2 = 1;
        #13;
        in1 = 1; in2 = 0;
    end

    top u_top
    (
        .and_out(and_out),
        .in1(in1),
        .in2(in2),
        .clk(clk)
    );

    initial begin
        $sdf_annotate("/home/wangyuankun/proj/Digital_Circuit/hdl/sdf_annotate/sim_test.sdf", u_top, , "sdf.log", "MAXIMUM", ,);
    end

    initial begin
        $fsdbDumpfile("test.fsdb");
        $fsdbDumpvars(0, top);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000) $finish;
        end
    end

endmodule
