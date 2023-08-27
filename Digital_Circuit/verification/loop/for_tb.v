// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/08/27 12:18
// Last Modified : 2023/08/27 12:23
// File Name     : for_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/08/27   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module for_tb;

    integer i;
    reg [3:0] counter;
    initial begin
        counter = 4'b0;
        for (i=0;i<=10;i=i+1) begin
            #10;
            counter = counter + 1'b1;
        end
    end

    initial begin
        $fsdbDumpfile("for.fsdb");
        $fsdbDumpvars(0, for_tb);
    end

    always begin
        #10;
        if ($time >= 1000)
            $finish;
    end

endmodule
