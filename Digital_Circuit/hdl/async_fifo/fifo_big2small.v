// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/22 18:53
// Last Modified : 2024/06/22 19:11
// File Name     : fifo_big2small.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/06/22   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module fifo_big2small
(
    input rstn,
    input [16-1:0] din,
    input din_clk,
    input din_en,

    output [4-1:0] dout,
    input dout_clk,
    output dout_en
);

    wire fifo_empty, fifo_full, prog_full;
    wire rd_en;
    wire [3:0] dout_wire;

    assign rd_en = fifo_empty ? 1'b0 : 1'b1;

    fifo
    #(
        .ADDRESS_WRITE_IN(3),
        .ADDRESS_WRITE_OUT(5),
        .DATA_WRITE_IN(16),
        .DATA_WRITE_OUT(4),
        .PROG_DEPTH(16)
    )
    u_fifo_big2small
    (
        .rstn(rstn),
        .wclk(din_clk),
        .wen(din_en),
        .wdata(din),

        .rclk(dout_clk),
        .ren(rd_en),
        .rdata(dout_wire),

        .wfull(fifo_full),
        .rempty(fifo_empty),
        .prog_full(proj_full)
    );

    reg dout_en_r;
    always @ (posedge dout_clk or negedge rstn) begin
        if (~rstn) begin
            dout_en_r <= 1'b0;
        end
        else begin
            dout_en_r <= rd_en;
        end
    end

    assign dout = dout_wire;
    assign dout_en = dout_en_r;

endmodule
