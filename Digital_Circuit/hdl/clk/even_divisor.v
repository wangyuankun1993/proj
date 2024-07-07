// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/06 18:49
// Last Modified : 2024/07/07 08:54
// File Name     : even_divisor.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/07/06   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module even_divisor
#(
    parameter DIV_CLK = 10
)
(
    input rstn,
    input clk,
    output clk_div2,
    output clk_div4,
    output clk_div10
);

// 2-divider
    reg clk_div2_r;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            clk_div2_r <= 1'b0;
        end
        else begin
            clk_div2_r <= ~clk_div2_r;
        end
    end
    assign clk_div2 = clk_div2_r;

// 4-divider
    reg clk_div4_r;
    always @ (posedge clk_div2 or negedge rstn) begin
        if (~rstn) begin
            clk_div4_r <= 1'b0;
        end
        else begin
            clk_div4_r <= ~clk_div4_r;
        end
    end
    assign clk_div4 = clk_div4_r;

// N/2 counter
    reg [3:0] cnt;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            cnt <= 4'b0;
        end
        else if (cnt == (DIV_CLK/2)-1) begin
            cnt <= 4'b0;
        end
        else begin
            cnt <= cnt + 1'b1;
        end
    end

    reg clk_div10_r;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            clk_div10_r <= 1'b0;
        end
        else if (cnt == (DIV_CLK/2)-1) begin
            clk_div10_r <= ~clk_div10_r;
        end
    end
    assign clk_div10 = clk_div10_r;

endmodule
