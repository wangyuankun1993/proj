// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/08/17 18:10
// Last Modified : 2024/08/17 18:18
// File Name     : mul2_ls.v
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
module mul2_ls
(
    input clk, // 100MHz
    input rstn,
    input en,
    input [3:0] mul1,
    input [3:0] mul2,
    input [3:0] mul3,
    input [3:0] mul4,
    output dout_en,
    output [8:0] dout
);

    wire [7:0] result1 = mul1 * mul2;
    wire [7:0] result2 = mul3 * mul4;

    reg en_r;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            en_r <= 1'b0;
        end
        else begin
            en_r = en;
        end
    end

    reg [7:0] res1_r, res2_r;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            res1_r <= 8'b0;
            res2_r <= 8'b0;
        end
        else if (en) begin
            res1_r <= result1;
            res2_r <= result2;
        end
    end

    assign dout = res1_r + res2_r;
    assign dout_en = en_r;

endmodule
