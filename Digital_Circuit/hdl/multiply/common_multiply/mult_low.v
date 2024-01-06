// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/01/06 14:55
// Last Modified : 2024/01/06 16:16
// File Name     : mult_low.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/01/06   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module mult_low
    # (parameter N=4, parameter M=4)
    (
        input clk,
        input rst_n,
        input data_rdy, // data input enable
        input [N-1:0] mult1, // multiplicand
        input [M-1:0] mult2, // multiplier

        output result_rdy, // data output enable
        output [N+M-1:0] result
    );

    // calculate counter
    reg [31:0] cnt;
    // multiply cycle counter
    wire [31:0] cnt_temp = (cnt == M) ? 'b0 : cnt + 1'b1;
    always @ (posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            cnt <= 'b0;
        end
        else if (data_rdy) begin // count when data enable
            cnt <= cnt_temp;
        end
        else if (cnt != 0) begin // avoid too short time for input enable
            cnt <= cnt_temp;
        end
        else begin
            cnt <= 'b0;
        end
    end

    // multiply
    reg [M-1:0] mult2_shift;
    reg [M+N-1:0] mult1_shift;
    reg [M+N-1:0] mult1_acc;
    always @ (posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            mult2_shift <= 'b0;
            mult1_shift <= 'b0;
            mult1_acc <= 'b0;
        end
        else if (data_rdy && cnt == 'b0) begin // initial
            mult1_shift <= {{(N){1'b0}}, mult1} << 1;
            mult2_shift <= mult2 >> 1;
            mult1_acc <= mult2[0] ? {{(N){1'b0}}, mult1} : 'b0;
        end
        else if (cnt != M) begin
            mult1_shift <= mult1_shift << 1; // multiplicand multiply 2
            mult2_shift <= mult2_shift >> 1; // multiplier shift right
            // check multiplier 1, 1 for accumulate
            mult1_acc <= mult2_shift[0] ? mult1_acc + mult1_shift : mult1_acc;
        end
        else begin
            mult2_shift <= 'b0;
            mult1_shift <= 'b0;
            mult1_acc <= 'b0;
        end
    end

    // result
    reg [M+N-1:0] result_r;
    reg result_rdy_r;
    always @ (posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            result_r <= 'b0;
            result_rdy_r <= 1'b0;
        end
        else if (cnt == M) begin
            result_r <= mult1_acc; // output result after multiply cycle end
            result_rdy_r <= 1'b1;
        end
        else begin
            result_r <= 'b0;
            result_rdy_r <= 1'b0;
        end
    end

    assign result = result_r;
    assign result_rdy = result_rdy_r;

endmodule
