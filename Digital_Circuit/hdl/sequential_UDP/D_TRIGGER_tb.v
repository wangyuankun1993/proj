// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/04/15 23:14
// Last Modified : 2024/04/15 23:25
// File Name     : D_TRIGGER_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/04/15   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module D_TRIGGER_tb;

    reg D, CP = 0;
    reg RST;
    wire Q;
    always #5 CP = ~CP;
    initial begin
        D = 0;
        #12 D = 1;
        #10 D = 0;
        #14 D = 1;
        #3 D = 0;
        #18 D = 0;
    end

    initial begin
        RST = 0;
        #3 RST = 1;
        #2 RST = 0;
        #22 RST = 1;
        #1 RST = 0;
    end

    D_TRIGGER u_D_TRIGGER(Q, RST, CP, D);

    initial begin
        forever begin
            #100;
            if ($time > 1000) begin
                $finish;
            end
        end
    end

    initial begin
        $fsdbDumpfile("D_TRIGGER.fsdb");
        $fsdbDumpvars(0, D_TRIGGER_tb);
    end

endmodule
