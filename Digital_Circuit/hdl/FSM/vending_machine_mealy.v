// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/10/07 23:43
// Last Modified : 2023/10/13 00:07
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
module vending_machine_mealy(
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

    // (2) state switch, using block assignment for combination-logic
    // all case items need to be displayed completely
    always @ (*) begin
        case(current_state)
            IDLE:
                case(coin)
                    2'b01: next_state = GET05;
                    2'b10: next_state = GET10;
                    default: next_state = IDLE;
                endcase
            GET05:
                case(coin)
                    2'b01: next_state = GET10;
                    2'b10: next_state = GET15;
                    default: next_state = GET05;
                endcase
            GET10:
                case(coin)
                    2'b01: next_state = GET15;
                    2'b10: next_state = IDLE;
                    default: next_state = GET10;
                endcase
            GET15:
                case(coin)
                    2'b01, 2'b10: next_state = IDLE;
                    default: next_state = GET15;
                endcase
            default: next_state = IDLE;
        endcase
    end

    // (3) output logic, using non-block assignment
    reg [1:0] change_r;
    reg sell_r;
    always @ (posedge clk or negedge rstn) begin
        if (!rstn) begin
            change_r <= 2'b0;
            sell_r <= 1'b0;
        end
        else if ((current_state == GET15 && coin  == 2'b01) || (current_state == GET10 && coin == 2'b10)) begin
            change_r <= 2'b0;
            sell_r <= 1'b1;
        end
        else if (current_state == GET15 && coin == 2'b10) begin
            change_r <= 2'b1;
            sell_r <= 1'b1;
        end
        else begin
            change_r <= 2'b0;
            sell_r <= 1'b0;
        end
    end

    assign sell = sell_r;
    assign change = change_r;

endmodule
