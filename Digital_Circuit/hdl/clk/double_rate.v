// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/02 22:46
// Last Modified : 2024/07/06 16:54
// File Name     : double_rate.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/07/02   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module double_rate
(
    input rstn,
    input clk,
    input csn,
    input [7:0] din,
    input din_en,
    output [7:0] dout,
    output dout_en
);

    // capture at posedge
    reg [7:0] datap_r;
    reg datap_en_r;
    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            datap_r <= 8'b0;
            datap_en_r <= 1'b0;
        end
        else if (din_en) begin
            datap_r <= din;
            datap_en_r <= 1'b1;
        end
        else begin
            datap_en_r <= 1'b0;
        end
    end

    // capture at posedge
    reg [7:0] datan_r;
    reg datan_en_r;
    always @ (negedge clk or negedge rstn) begin
        if (~rstn) begin
            datan_r <= 8'b0;
            datan_en_r <= 1'b0;
        end
        else if (din_en) begin
            datan_r <= din;
            datan_en_r <= 1'b1;
        end
        else begin
            datan_en_r <= 1'b0;
        end
    end

    assign dout = ~csn ? datap_r : datan_r;
    assign dout_en = datap_en_r | datan_en_r;

endmodule
