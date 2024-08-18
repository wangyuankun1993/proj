// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/08/17 17:59
// Last Modified : 2024/08/17 18:10
// File Name     : mul1_hs.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/08/17   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module mul1_hs
(
    input clk, // 200MHz
    input rstn,
    input en,
    input [3:0] mul1,
    input [3:0] mul2,
    output dout_en,
    output [8:0] dout
);

    reg flag;
    reg en_r;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            flag <= 1'b0;
            en_r <= 1'b0;
        end
        else if (en) begin
            flag <= ~flag;
            en_r <= 1'b1;
        end
        else begin
            flag <= 1'b0;
            en_r <= 1'b0;
        end
    end

    wire [7:0] result = mul1 * mul2;

    reg [7:0] res1_r, res2_r;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            res1_r <= 8'b0;
            res2_r <= 8'b0;
        end
        else if (en & ~flag) begin
            res1_r <= result;
        end
        else if (en & flag) begin
            res2_r <= result;
        end
    end

    assign dout_en = en_r & ~flag;
    assign dout = res1_r + res2_r;

endmodule
