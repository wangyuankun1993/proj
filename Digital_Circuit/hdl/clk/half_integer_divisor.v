// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/07 17:18
// Last Modified : 2024/07/07 18:58
// File Name     : half_integer_divisor.v
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
module half_integer_divisor
(
    input rstn,
    input clk,
    output clk_div3p5
);

    parameter MUL2_DIV_CLK = 7;
    reg [3:0] cnt;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            cnt <= 4'b0;
        end
        else if (cnt == MUL2_DIV_CLK-1) begin
            cnt <= 4'b0;
        end
        else begin
            cnt <= cnt + 1'b1;
        end
    end

    reg clk_ave_r;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            clk_ave_r <= 1'b0;
        end
        // first cycle: 4 source clk cycle
        else if (cnt == 0) begin
            clk_ave_r <= 1'b1;
        end
        // second cycle: 3 source clk cycle
        else if (cnt == (MUL2_DIV_CLK>>1)+1) begin
            clk_ave_r <= 1'b1;
        end
        else begin
            clk_ave_r <= 1'b0;
        end
    end

    reg clk_adjust_r;
    always @ (negedge clk or negedge rstn) begin
        if (~rstn) begin
            clk_adjust_r <= 1'b0;
        end
        else if (cnt == 1) begin
            clk_adjust_r <= 1'b1;
        end
        else if (cnt == (MUL2_DIV_CLK>>1)+1) begin
            clk_adjust_r <= 1'b1;
        end
        else begin
            clk_adjust_r <= 1'b0;
        end
    end

    assign clk_div3p5 = clk_adjust_r | clk_ave_r;

endmodule
