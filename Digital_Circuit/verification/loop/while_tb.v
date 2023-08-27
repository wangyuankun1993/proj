// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/08/27 11:58
// Last Modified : 2023/08/27 12:03
// File Name     : while_tb.v
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
module while_tb;

    reg [3:0] counter;
    initial begin
        counter = 4'b0;
        while (counter <= 10) begin
            #10;
            counter = counter + 1'b1;
        end
    end

    initial begin
        $fsdbDumpfile("while.fsdb");
        $fsdbDumpvars(0, while_tb);
    end

    always begin
        #10;
        if ($time >= 1000)
            $finish;
    end

endmodule
