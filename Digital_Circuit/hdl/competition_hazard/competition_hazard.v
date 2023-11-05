// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/11/05 23:29
// Last Modified : 2023/11/05 23:32
// File Name     : competition_hazard.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/11/05   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module competition_hazard(
    input clk,
    input rst_n,
    input en,
    input din_rvs,
    output reg flag
);

    wire condition = din_rvs & en; // combination logic
    always @ (posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            flag <= 1'b0;
        end
        else begin
            flag <= condition;
        end
    end

endmodule
