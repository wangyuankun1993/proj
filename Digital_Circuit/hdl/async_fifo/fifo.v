// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/16 19:04
// Last Modified : 2024/06/23 15:36
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

    generate
    // small data in, big data out
        if (DATA_WRITE_OUT >= DATA_WRITE_IN) begin: EXTEND_WIDTH
            // gray code transfer
            wire [ADDRESS_WRITE_IN:0] wptr = ({wover_flag, waddr}) ^ ({wover_flag, waddr} >> 1);
            // sync write data pointer to read clk domain
            reg [ADDRESS_WRITE_IN:0] rq2_wptr_r0;
            reg [ADDRESS_WRITE_IN:0] rq2_wptr_r1;
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
            
            // gray code transfer
            wire [ADDRESS_WRITE_IN-1:0] raddr_extend = raddr << EXTENT_BIT;
            wire [ADDRESS_WRITE_IN:0] rptr = ({rover_flag, raddr_extend}) ^ ({rover_flag, raddr_extend} >> 1);
            // sync read data pointer to write clk domain
            reg [ADDRESS_WRITE_IN:0] wq2_rptr_r0;
            reg [ADDRESS_WRITE_IN:0] wq2_rptr_r1;
            always @ (posedge wclk or negedge rstn) begin
                if (~rstn) begin
                    wq2_rptr_r0 <= 'b0;
                    wq2_rptr_r1 <= 'b0;
                end
                else begin
                    wq2_rptr_r0 <= rptr;
                    wq2_rptr_r1 <= wq2_rptr_r0;
                end
            end

            // gray code decode
            reg [ADDRESS_WRITE_IN:0] wq2_rptr_decode;
            reg [ADDRESS_WRITE_IN:0] rq2_wptr_decode;
            integer i;
            always @ (*) begin
                wq2_rptr_decode[ADDRESS_WRITE_IN] = wq2_rptr_r1[ADDRESS_WRITE_IN];
                for (i=ADDRESS_WRITE_IN-1; i>=0; i=i-1) begin
                    wq2_rptr_decode[i] = wq2_rptr_decode[i+1] ^ wq2_rptr_r1[i];
                end
            end
            always @ (*) begin
                rq2_wptr_decode[ADDRESS_WRITE_IN] = rq2_wptr_r1[ADDRESS_WRITE_IN];
                for (i=ADDRESS_WRITE_IN-1; i>=0; i=i-1) begin
                    rq2_wptr_decode[i] = rq2_wptr_decode[i+1] ^ rq2_wptr_r1[i];
                end
            end

            // read/write address and extend_bit identical, empty
            assign rempty = (rover_flag == rq2_wptr_decode[ADDRESS_WRITE_IN]) && (raddr_extend >= rq2_wptr_decode[ADDRESS_WRITE_IN-1:0]);

            // read/write address identical, extend_bit different, full
            assign wfull = (wover_flag != wq2_rptr_decode[ADDRESS_WRITE_IN]) && (waddr >= wq2_rptr_decode[ADDRESS_WRITE_IN-1:0]);

            // extend_bit identical, write address no less than read address; extend_bit different, while write address less than read address, the actual write address need add a FIFO depth
            assign prog_full = (wover_flag == wq2_rptr_decode[ADDRESS_WRITE_IN]) ?
                waddr - wq2_rptr_decode[ADDRESS_WRITE_IN-1:0] >= PROG_DEPTH - 1 :
                waddr + (ADDRESS_WRITE_IN << 1) - wq2_rptr_decode[ADDRESS_WRITE_IN-1:0] >=PROG_DEPTH - 1;

            dual_port_ram
            #(
                .ADDRESS_WRITE_IN(ADDRESS_WRITE_IN),
                .ADDRESS_WRITE_OUT(ADDRESS_WRITE_OUT),
                .DATA_WRITE_IN(DATA_WRITE_IN),
                .DATA_WRITE_OUT(DATA_WRITE_OUT)
            )
            u_dual_port_ram
            (
                .CLK_WR(wclk),
                .WR_EN(wen && !wfull),
                .ADDR_WR(waddr),
                .D(wdata[DATA_WRITE_IN-1:0]),
                .CLK_RD(rclk),
                .RD_EN(ren && !rempty),
                .ADDR_RD(raddr),
                .Q(rdata[DATA_WRITE_OUT-1:0])
            );
        end
    // big in and smalla out
        else begin: // SHRINK_WIDTH
            // gray code
            wire [ADDRESS_WRITE_OUT-1:0] waddr_extend = waddr << SHRINK_BIT;
            wire [ADDRESS_WRITE_OUT:0] wptr = {wover_flag, waddr_extend} ^ ({wover_flag, waddr_extend} >> 1);
            reg [ADDRESS_WRITE_OUT:0] rq2_wptr_r0;
            reg [ADDRESS_WRITE_OUT:0] rq2_wptr_r1;
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

            wire [ADDRESS_WRITE_OUT:0] rptr = {rover_flag, raddr} ^ ({rover_flag, raddr} >> 1);
            reg [ADDRESS_WRITE_OUT:0] wq2_rptr_r0;
            reg [ADDRESS_WRITE_OUT:0] wq2_rptr_r1;
            always @ (posedge wclk or negedge rstn) begin
                if (~rstn) begin
                    wq2_rptr_r0 <= 'b0;
                    wq2_rptr_r1 <= 'b0;
                end
                else begin
                    wq2_rptr_r0 <= rptr;
                    wq2_rptr_r1 <= wq2_rptr_r0;
                end
            end

            reg [ADDRESS_WRITE_OUT:0] wq2_rptr_decode;
            reg [ADDRESS_WRITE_OUT:0] rq2_wptr_decode;
            integer i;
            always @ (*) begin
                wq2_rptr_decode[ADDRESS_WRITE_OUT] = wq2_rptr_r1[ADDRESS_WRITE_OUT];
                for (i=ADDRESS_WRITE_OUT-1; i>=0; i=i-1) begin
                    wq2_rptr_decode[i] = wq2_rptr_decode[i+1] ^ wq2_rptr_r1[i];
                end
            end
            always @ (*) begin
                rq2_wptr_decode[ADDRESS_WRITE_OUT] = rq2_wptr_r1[ADDRESS_WRITE_OUT];
                for (i=ADDRESS_WRITE_OUT-1; i>=0; i=i-1) begin
                    rq2_wptr_decode[i] = rq2_wptr_decode[i+1] ^ rq2_wptr_r1[i];
                end
            end

            // read/write address and extend_bit identical, empty
            assign rempty = (rover_flag == rq2_wptr_decode[ADDRESS_WRITE_OUT]) && (raddr >= rq2_wptr_decode[ADDRESS_WRITE_OUT-1:0]);

            // read/write address identical, extend_bit different, full
            assign wfull = (wover_flag != wq2_rptr_decode[ADDRESS_WRITE_OUT]) && (waddr_extend >= wq2_rptr_decode[ADDRESS_WRITE_OUT-1:0]);

            // extend_bit identical, write address no less than read address; extend_bit different, while write address less than read address, the actual write address need add a FIFO depth
            assign prog_full = (wover_flag == wq2_rptr_decode[ADDRESS_WRITE_OUT]) ?
                waddr_extend - wq2_rptr_decode[ADDRESS_WRITE_OUT-1:0] >= PROG_DEPTH - 1 :
                waddr_extend + (ADDRESS_WRITE_OUT << 1) - wq2_rptr_decode[ADDRESS_WRITE_OUT-1:0] >=PROG_DEPTH - 1;

            dual_port_ram
            #(
                .ADDRESS_WRITE_IN(ADDRESS_WRITE_IN),
                .ADDRESS_WRITE_OUT(ADDRESS_WRITE_OUT),
                .DATA_WRITE_IN(DATA_WRITE_IN),
                .DATA_WRITE_OUT(DATA_WRITE_OUT)
            )
            u_dual_port_ram
            (
                .CLK_WR(wclk),
                .WR_EN(wen && !wfull),
                .ADDR_WR(waddr),
                .D(wdata[DATA_WRITE_IN-1:0]),
                .CLK_RD(rclk),
                .RD_EN(ren && !rempty),
                .ADDR_RD(raddr),
                .Q(rdata[DATA_WRITE_OUT-1:0)
            );
        end
    endgenerate

endmodule
