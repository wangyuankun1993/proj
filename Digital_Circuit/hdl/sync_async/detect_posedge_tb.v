// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/05/29 22:07
// Last Modified : 2024/05/29 22:18
// File Name     : detect_posedge_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/05/29   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module detect_posedge_tb;

    reg d;
    reg clk;
    reg rstn;
    wire q;

    always #5 clk = ~clk;

    initial begin
        clk = 1'b0;
        rstn = 1'b0;
        #13;
        rstn = 1'b1;
    end

    initial begin
        d = 1'b0;
        #10;
        d = 1'b1;
        #20;
        d = 1'b0;
        #30;
        d = 1'b1;
    end

    detect_posedge u_detect_posedge
    (
        .q(q),
        .clk(clk),
        .rstn(rstn),
        .d(d)
    );

    initial begin
        $fsdbDumpfile("detect_posedge.fsdb");
        $fsdbDumpvars(0, detect_posedge_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000) $finish;
        end
    end

endmodule
