// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/03/24 21:53
// Last Modified : 2024/03/24 22:10
// File Name     : D_Trigger_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/03/24   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module D_Trigger_tb;
    reg D, CP = 0;
    wire Q, QR;
    always #5 CP = ~CP;
    initial begin
        D = 0;
        #12 D = 1;
        #10 D = 0;
        #14 D = 1;
        #3 D = 0;
        #18 D = 0;
    end

    D_Trigger u_D_Trigger
    (
        .D(D),
        .CP(CP),
        .Q(Q),
        .QR(QR)
    );

    initial begin
        $fsdbDumpfile("D_Trigger.fsdb");
        $fsdbDumpvars(0, D_Trigger_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000) begin
                $finish;
            end
        end
    end
endmodule
