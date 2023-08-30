// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/08/30 00:45
// Last Modified : 2023/08/31 00:06
// File Name     : dff_assign_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/08/30   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module dff_assign_tb;

    reg rstn;
    reg clk;
    reg D;
    wire Q;

    initial begin
        rstn = 1'b1;
        D = 1'b0;
        #5;
        rstn = 1'b0;
        #10;
        rstn = 1'b1;
        #20;
        D = 1'b1;
        #20;
        D = 1'b0;
    end

    initial begin
        clk = 1'b0;
        forever begin
            clk = ~clk;
            #5;
        end
    end

    dff_assign u_dff_assign(
        .rstn(rstn),
        .clk(clk),
        .D(D),
        .Q(Q)
    );

    initial begin
        $fsdbDumpfile("dff_assign.fsdb");
        $fsdbDumpvars(0, dff_assign_tb);
    end

    always begin
        #10;
        if ($time >= 1000)
            $finish;
    end

endmodule
