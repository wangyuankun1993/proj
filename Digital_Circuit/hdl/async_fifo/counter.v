// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/16 17:51
// Last Modified : 2024/06/16 17:54
// File Name     : counter.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/06/16   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module counter
#(
    parameter W
)
(
    input rstn,
    input clk,
    input en,
    output [W-1:0] count
);

    reg [W-1:0] count_r;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            count_r <= 'b0;
        end
        else if (en) begin
            count_r <= count_r + 1'b1;
        end
    end
    assign count = count_r;

endmodule
