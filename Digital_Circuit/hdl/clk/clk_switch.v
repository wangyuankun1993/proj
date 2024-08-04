// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/28 23:25
// Last Modified : 2024/08/04 23:57
// File Name     : clk_switch.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/07/28   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module clk_switch
(
    input rstn,
    input clk1,
    input clk2,
    input sel_clk1, // 1 clk1, 0 clk2
    output clk_out
);

    reg [2:0] sel_clk1_r;
    reg [1:0] sel_clk1_neg_r;
    reg [2:0] sel_clk2_r;
    reg [1:0] sel_clk2_neg_r;

    // 3-stage sync, sync another domain clk enable "and" with current domain clk enable
    always @ (posedge clk1 or negedge rstn) begin
        if (~rstn) begin
            sel_clk1_r <= 3'b111;
        end
        else begin
            sel_clk1_r <= {sel_clk1_r[1:0], sel_clk1 & ~sel_clk2_neg_r[1]};
        end
    end

    // in negedge clk, 2-stage sync clk enable
    always @ (negedge clk1 or negedge rstn) begin
        if (~rstn) begin
            sel_clk1_neg_r <= 2'b11;
        end
        else begin
            sel_clk1_neg_r <= {sel_clk1_neg_r[0], sel_clk1_r[2]};
        end
    end

    // 3-stage sync, sync another domain clk enable "and" with current domain clk enable
    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            sel_clk2_r <= 3'b0;
        end
        else begin
            sel_clk2_r <= {sel_clk2_r[1:0], ~sel_clk1 & ~sel_clk1_neg_r[1]};
        end
    end

    // in negedge clk, 2-stage sync clk enable
    always @ (negedge clk2 or negedge rstn) begin
        if (~rstn) begin
            sel_clk2_neg_r <= 2'b0;
        end
        else begin
            sel_clk2_neg_r <= {sel_clk2_neg_r[0], sel_clk2_r[2]};
        end
    end

    // clk logic function, use specific process library
    // use Verilog build-in logic gate cell
    wire clk1_gate, clk2_gate;
    and u_clk1_gate (clk1_gate, clk1, sel_clk1_neg_r[1]);
    and u_clk2_gate (clk2_gate, clk2, sel_clk2_neg_r[1]);
    or u_clk_or (clk_out, clk1_gate, clk2_gate);

endmodule
