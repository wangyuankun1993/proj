// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/02/03 17:58
// Last Modified : 2024/02/22 23:08
// File Name     : divider_man.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/02/03   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module divider_man
    #(
        parameter N=5,
        parameter M=3,
        parameter N_ACT=M+N-1
    )
    (
        input clk,
        input rst_n,

        input data_enable,
        input [N-1:0] dividend,
        input [M-1:0] divisor,

        output result_ready,
        output [N_ACT-M:0] merchant,
        output [M-1:0] remainder
    );

    wire [N_ACT-M-1:0] dividend_t [N_ACT-M:0];
    wire [M-1:0] divisor_t [N_ACT-M:0];
    wire [M-1:0] remainder_t [N_ACT-M:0];
    wire [N_ACT-M:0] ready_t;
    wire [N_ACT-M:0] merchant_t [N_ACT-M:0];

    // initial first cell
    divider_cell #(.N(N_ACT), .M(M)) u_divider_step0
    (
        .clk(clk),
        .rst_n(rst_n),
        .en(data_enable),
        // The MSB 1 bit of initial dividend used as dividend of first step divider, high bit complete with 0
        .dividend({{(M){1'b0}}, dividend[N-1]}),
        .divisor(divisor),
        .merchant_ci({(N_ACT-M+1){1'b0}}), // initial merchant is 0
        .dividend_ci(dividend[N_ACT-M-1:0]), // initial dividend
        .dividend_kp(dividend_t[N_ACT-M]), // initial dividend info transfer
        .divisor_kp(divisor_t[N_ACT-M]), // initial divisor info transfer
        .ready(ready_t[N_ACT-M]),
        .merchant(merchant_t[N_ACT-M]), // first merchant result
        .remainder(remainder_t[N_ACT-M]) // first remainder result
    );

    genvar i;
    generate
        for(i=1; i<=N_ACT-M; i=i+1) begin: sqrt_stepx
            divider_cell #(.N(N_ACT), .M(M)) u_divider_step
            (
                .clk(clk),
                .rst_n(rst_n),
                .en(rdy_t[N_ACT-M-i+1]),
                .dividend({remainder_t[N_ACT-M-i+1], dividend_t[N_ACT-M-i+1][N_ACT-M-i]}), // remainder together with initial dividend sigle bit data
                .divisor(divisor_t[N_ACT-M-i+1]),
                .merchant_ci(merchant_t[N_ACT-M-i+1]),
                .dividend_ci(dividend_t[N_ACT-M-i+1]),
                // output
                .divisor_kp(divisor_t[N_ACT-M-i]),
                .dividend_kp(dividend_t[N_ACT-M-i]),
                .ready(ready_t[N_ACT-M-i]),
                .merchant(merchant_t[N_ACT-M-i]),
                .remainder(remainder_t[N_ACT-M-i])
            );
        end
    endgenerate

    assign result_ready = ready_t[0];
    assign merchant = merchant_t[0]; // last merchant as final merchant
    assign remainder = remainder_t[0]; // last remainder as final remainder

endmodule
