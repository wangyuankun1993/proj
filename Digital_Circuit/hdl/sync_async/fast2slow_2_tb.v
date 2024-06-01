// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/01 15:02
// Last Modified : 2024/06/01 17:16
// File Name     : fast2slow_2_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/06/01   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module fast2slow_2_tb;

    reg clk_slow;
    reg clk_fast;
    reg rstn;

    initial begin
        clk_slow = 1'b0;
        clk_fast = 1'b0;
        rstn = 1'b0;
        #11 rstn = 1'b1;
    end

    always #10 clk_fast = ~clk_fast;
    always @ (posedge clk_fast)
        clk_slow = ~clk_slow;

    fast2slow_2 u_fast2slow_2
    (
        .rstn(rstn),
        .clk1(clk_fast),
        .clk2(clk_slow),
        .sig22()
    );

    initial begin
        $fsdbDumpfile("fast2slow_2.fsdb");
        $fsdbDumpvars(0, fast2slow_2_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000) $finish;
        end
    end

endmodule
