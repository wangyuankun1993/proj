// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/23 22:30
// Last Modified : 2024/06/23 22:35
// File Name     : areset_srelease.v
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
module areset_srelease
(
    input rstn,
    input clk,
    input din,
    output reg dout
);

    reg rstn_r1, rstn_r2;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            rstn_r1 <= 1'b0; // async reset
            rstn_r2 <= 1'b0;
        end
        else begin
            rstn_r1 <= 1'b1; // sync release
            rstn_r2 <= rstn_r1;
        end
    end

    always @ (posedge clk or negedge rstn_r2) begin
        if (~rstn_r2) begin
            dout <= 1'b0;
        end
        else begin
            dout <= din;
        end
    end

endmodule
