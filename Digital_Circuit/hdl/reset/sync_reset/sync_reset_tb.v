// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/23 17:01
// Last Modified : 2024/06/23 17:41
// File Name     : sync_reset_tb.v
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

module sync_reset_tb;

    reg rstn;
    reg clk;
    reg din;
    wire dout;

    initial begin
        clk = 1'b0;
        rstn = 1'b0;
        #13 rstn = 1'b1;
    end

    always #5 clk = ~clk;

    initial begin
        din = 1'b0;
        #13 din = 1'b1;
        #17 din = 1'b0;
        #23 din = 1'b1;
    end

    sync_reset u_sync_reset
    (
        .rstn(rstn),
        .clk(clk),
        .din(din),
        .dout(dout)
    );

    initial begin
        forever begin
            #100;
            if ($time >= 1000) $finish;
        end
    end

    initial begin
        $fsdbDumpfile("sync_reset.fsdb");
        $fsdbDumpvars(0, sync_reset_tb);
    end

endmodule
