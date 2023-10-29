// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/10/14 12:27
// Last Modified : 2023/10/14 12:46
// File Name     : vending_machine_moore.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/10/14   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module vending_machine_moore(
    input clk,
    input rstn,
    input [1:0] coin, // 01 for 0.5 jiao, 10 for 1 yuan
    output [1:0] change,
    output sell // output the drink
);

    // machine state decode
    parameter IDLE = 3'd0;
    parameter GET05 = 3'd1;
    parameter GET10 = 3'd2;
    parameter GET15 = 3'd3;
    parameter GET20 = 3'd4;
    parameter GET25 = 3'd5;

    // machine variable
    reg [2:0] next_state;
    reg [2:0] current_state;

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
    always @ (*) begin // all case items need to be displayed completely
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
                    2'b10: next_state = GET20;
                    default: next_state = GET10;
                endcase
            GET15:
                case(coin)
                    2'b01: next_state = GET20;
                    2'b10: next_state = GET25;
                    default: next_state = GET15;
                endcase
            GET20:
                next_state = IDLE;
            GET25:
                next_state = IDLE;
            default: next_state = IDLE;
        endcase
    end

    // (3) output logic
    // one cycle delayed when using non-block assignment
    reg [1:0] change_r;
    reg sell_r;
    always @ (posedge clk or negedge rstn) begin
        if (!rstn) begin
            change_r <= 2'b0;
            sell_r <= 1'b0;
        end
        else if (current_state == GET20) begin
            sell_r <= 1'b1;
        end
        else if (current_state == GET25) begin
            change_r <= 2'b1;
            sell_r <= 1'b1;
        end
        else begin
            change_r <= 2'b0;
            sell_r <= 1'b0;
        end
    end

    assign change = change_r;
    assign sell = sell_r;

endmodule
