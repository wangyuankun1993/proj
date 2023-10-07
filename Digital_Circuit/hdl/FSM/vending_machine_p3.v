// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/10/07 23:43
// Last Modified : 2023/10/07 23:50
// File Name     : vending_machine_p3.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/10/07   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module vending_machine_p3(
    input clk,
    input rstn,
    input [1:0] coin, // 01 for 0.5 yuan, 10 for 1 yuan
    output [1:0] change,
    output sell //output the drink
);

    // machine state decode
    parameter IDLE = 3'd0;
    parameter GET05 = 3'd1;
    parameter GET10 = 3'd2;
    parameter GET15 = 3'd3;

    // machine variable
    reg [2:0] current_state;
    reg [2:0] next_state;

    // (1) state transfer
    always @ (posedge clk or negedge rstn) begin
        if (!rstn) begin
            current_state <= 3'b0;
        end
        else begin
            current_state <= next_state;
        end
    end
