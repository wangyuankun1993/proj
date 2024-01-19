// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/01/17 08:21
// Last Modified : 2024/01/18 08:36
// File Name     : mult_man.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/01/17   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module mult_man #(parameter N=4, parameter M=4)
    (
        input clk,
        input rst_n,
        input data_ready,
        input [N-1:0] mult1,
        input [M-1:0] mult2,

        output result_ready,
        output [N+M-1:0] result
    );

    wire [N+M-1:0] mult1_t [M-1:0];
    wire [M-1:0] mult2_t [M-1:0];
    wire [N+M-1:0] mult1_acc_t [M-1:0];
    wire [M-1:0] ready_t;

    // First instantiation the same as initial, can't use generate
    mult_cell #(.N(N), .M(M)) u_mult_step0
    (
        .clk(clk),
        .rst_n(rst_n),
        .en(data_ready),
        .mult1({{(M){1'b0}}, mult1}),
        .mult2(mult2),
        .mult1_acci({(N+M){1'b0}}),
        // output
        .mult1_acco(mult1_acc_t[0]),
        .mult2_shift(mult2_t[0]),
        .mult1_o(mult1_t[0]),
        .ready(ready_t[0])
    );

    // Multiple instantiation, use generate
    genvar i;
    generate
        for(i=1; i<=M-1; i=i+1) begin: mult_stepx
            mult_cell #(.N(N), .M(M)) u_mult_step
            (
                .clk(clk),
                .rst_n(rst_n),
                .en(ready_t[i-1]),
                .mult1(mult1_t[i-1]),
                .mult2(mult2_t[i-1]),
                .mult1_acci(mult1_acc_t[i-1]),
                // output
                .mult1_acco(mult1_acc_t[i]),
                .mult2_shift(mult2_t[i]),
                .mult1_o(mult1_t[i]),
                .ready(ready_t[i])
            );
        end
    endgenerate

    assign result_ready = ready_t[M-1];
    assign result = mult1_acc_t[M-1];

endmodule
