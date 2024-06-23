// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/23 18:37
// Last Modified : 2024/06/23 18:41
// File Name     : async_reset.v
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
module async_reset
(
    input rstn,
    input clk,
    input din,
    output reg dout
);

    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            dout <= 1'b0;
        end
        else begin
            dout <= din;
        end
    end

endmodule
