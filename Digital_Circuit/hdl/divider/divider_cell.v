// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/01/26 23:56
// Last Modified : 2024/02/03 18:29
// File Name     : divider_cell.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/01/26   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module divider_cell #(parameter N=5, parameter M=3)
    (
        input clk,
        input rst_n,
        input en,

        input [M:0] dividend,
        input [M-1:0] divisor,
        input [N-M:0] merchant_ci, // above level merchant
        input [N-M-1:0] dividend_ci, // initial dividend

        output reg [N-M-1:0] dividend_kp, // initial dividend
        output reg [M-1:0] divisor_kp, // initial divisor
        output reg ready,
        output reg [N-M:0] merchant,
        output reg [M-1:0] remainder
    );

    always @ (posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            ready <= 'b0;
            merchant <= 'b0;
            remainder <= 'b0;
            divisor_kp <= 'b0;
            dividend_kp <= 'b0;
        end
        else if (en) begin
            ready <= 1'b1;
            divisor_kp <= divisor; // initial divisor keep stable
            dividend_kp <= dividend_ci; // initial dividend transfer
            if (dividend >= {1'b0, divisor}) begin
                merchant <= (merchant_ci << 1) + 1'b1; // merchant is 1
                remainder <= dividend - {1'b0, divisor}; // remainder
            end
            else begin
                merchant <= merchant_ci << 1; // merchant is 0
                remainder <= dividend; // remainder is stable
            end
        end
        else begin
            ready <= 'b0;
            merchant <= 'b0;
            remainder <= 'b0;
            divisor_kp <= 'b0;
            dividend_kp <= 'b0;
        end
    end

endmodule
