// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/02 12:35
// Last Modified : 2024/06/02 15:08
// File Name     : delay_sample.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/06/02   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module delay_sample
(
    input rstn,
    input clk1,
    input [31:0] din,
    input din_en,

    input clk2,
    output [31:0] dout,
    output dout_en
);

    // sync din_en
    reg [2:0] din_en_r;
    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            din_en_r <= 3'b0;
        end
        else begin
            din_en_r <= {din_en_r[1:0], din_en};
        end
    end

    wire din_en_pos;
    assign din_en_pos = din_en_r[1] & ~din_en_r[2];

    // sync data
    reg [31:0] dout_r;
    reg dout_en_r;
    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            dout_r <= 32'b0;
        end
        else if (din_en_pos) begin
            dout_r <= din;
        end
    end

    // dout_en delay
    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            dout_en_r <= 1'b0;
        end
        else begin
            dout_en_r <= din_en_pos;
        end
    end

    assign dout = dout_r;
    assign dout_en = dout_en_r;

endmodule
