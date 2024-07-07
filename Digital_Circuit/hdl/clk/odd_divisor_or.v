// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/07 09:37
// Last Modified : 2024/07/07 10:55
// File Name     : odd_divisor_or.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/07/07   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module odd_divisor_or
#(
    parameter DIV_CLK = 9
)
(
    input rstn,
    input clk,
    output clk_div9
);

    reg [3:0] cnt;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            cnt <= 4'b0;
        end
        else if (cnt == (DIV_CLK - 1)) begin
            cnt <= 4'b0;
        end
        else begin
            cnt <= cnt + 1'b1;
        end
    end

    reg clkp_div9_r;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            clkp_div9_r <= 1'b0;
        end
        else if (cnt == (DIV_CLK>>1)-1) begin
            clkp_div9_r <= 1'b0;
        end
        else if (cnt == DIV_CLK-1) begin
            clkp_div9_r <= 1'b1;
        end
    end

    reg clkn_div9_r;
    always @ (negedge clk or negedge rstn) begin
        if (~rstn) begin
            clkn_div9_r <= 1'b0;
        end
        else if (cnt == (DIV_CLK>>1)) begin
            clkn_div9_r <= 1'b0;
        end
        else if (cnt == 0) begin
            clkn_div9_r <= 1'b1;
        end
    end

    assign clk_div9 = clkp_div9_r | clkn_div9_r;

endmodule
