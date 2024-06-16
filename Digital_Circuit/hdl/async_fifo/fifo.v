// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/16 19:04
// Last Modified : 2024/06/16 23:21
// File Name     : fifo.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/06/16   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module fifo
#(
    parameter ADDRESS_WRITE_IN = 5,
    parameter ADDRESS_WRITE_OUT = 3,
    parameter DATA_WRITE_IN = 4,
    parameter DATA_WRITE_OUT = 16,
    parameter PROG_DEPTH = 16
)
(
    input rstn, // write/read reset
    input wclk, // write clk
    input wen, // write enable
    input [DATA_WRITE_IN-1:0] wdata, // write data

    input rclk, // read clk
    input ren, // read enable
    output [DATA_WRITE_OUT-1:0] rdata, // read data

    output wfull, // write full flag
    output rempty, // read empty flag
    output prog_full // programmable full flag
);

    // output width larger than input width
    parameter EXTENT = DATA_WRITE_OUT/DATA_WRITE_IN;
    parameter EXTENT_BIT = ADDRESS_WRITE_IN - ADDRESS_WRITE_OUT;
    // output width smaller than input width
    parameter SHRINK = DATA_WRITE_IN/DATA_WRITE_OUT;
    parameter SHRINK_BIT = ADDRESS_WRITE_OUT - ADDRESS_WRITE_IN;

    // ----------------------------push/wr counter-----------------------------
    wire [ADDRESS_WRITE_IN-1:0] waddr;
    wire wover_flag; // one more bit used as write address extend
    counter #(.W(ADDRESS_WRITE_IN+1)) u_push_counter
    (
        .rstn(rstn),
        .clk(wclk),
        .en(wen && !wfull),
        .count({wover_flag, waddr})
    );

    // ----------------------------pop/rd counter-----------------------------
    wire [ADDRESS_WRITE_OUT-1:0] raddr;
    wire rover_flag; // one more bit used as read address extend
    counter #(W(ADDRESS_WRITE_OUT+1)) u_pop_counter
    (
        .rstn(rstn),
        .clk(rclk),
        .en(ren && !rempty),
        .count({rover_flag, raddr})
    );

    // small data in, big data out
    generate
        if (DATA_WRITE_OUT >= DATA_WRITE_IN) begin: EXTEND_WIDTH
            // gray code transfer
            wire [ADDRESS_WRITE_IN-1:0] wptr = ({wover_flag, waddr}) ^ ({wover_flag, waddr} >> 1);
            // sync write data pointer to read clk domain
            reg [ADDRESS_WRITE_IN-1:0] rq2_wptr_r0;
            reg [ADDRESS_WRITE_IN-1:0] rq2_wptr_r1;
            always @ (posedge rclk or negedge rstn) begin
                if (~rstn) begin
                    rq2_wptr_r0 <= 'b0;
                    rq2_wptr_r1 <= 'b0;
                end
                else begin
                    rq2_wptr_r0 <= wptr;
                    rq2_wptr_r1 <= rq2_wptr_r0;
                end
            end
