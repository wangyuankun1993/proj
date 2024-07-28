// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/14 12:52
// Last Modified : 2024/07/28 13:21
// File Name     : frac_divisor.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/07/14   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module frac_divisor
#(
    parameter SOURCE_NUM = 76, // cycles in source clock
    parameter DEST_NUM = 10 // cycles in destination clock
)
(
    input rstn,
    input clk,
    output clk_frac
);

    parameter SOURCE_DIV = SOURCE_NUM/DEST_NUM;
    parameter DEST_DIV = SOURCE_DIV + 1;
    parameter DIFF_ACC = SOURCE_NUM - SOURCE_DIV*DEST_NUM;

    reg [3:0] cnt_end_r; // variation divider cycle
    reg [3:0] main_cnt; // main counter
    reg clk_frac_r; // clk output

    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            main_cnt <= 4'b0;
            clk_frac_r <= 1'b0;
        end
        else if (main_cnt == cnt_end_r) begin
            main_cnt <= 4'b0;
            clk_frac_r <= 1'b1;
        end
        else begin
            main_cnt <= main_cnt + 1'b1;
            clk_frac_r <= 1'b0;
        end
    end

    // output clk
    assign clk_frac = clk_frac_r;

    // differential value accumulate enable
    wire diff_cnt_en = main_cnt == cnt_end_r;

    // differential value accumulate
    reg [4:0] diff_cnt_r;
    wire [4:0] diff_cnt = diff_cnt_r >= DEST_NUM ?
                          diff_cnt_r - 10 + DIFF_ACC :
                          diff_cnt_r + DIFF_ACC;

    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            diff_cnt_r <= 5'b0;
        end
        else if (diff_cnt_en) begin
            diff_cnt_r <= diff_cnt;
        end
    end

    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            cnt_end_r <= SOURCE_DIV-1;
        end
        else if (diff_cnt >= 10) begin
            cnt_end_r <= DEST_DIV-1;
        end
        else begin
            cnt_end_r <= SOURCE_DIV-1;
        end
    end

endmodule
