// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/02 16:30
// Last Modified : 2024/06/02 16:57
// File Name     : delay_cnt_sample.v
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
module delay_cnt_sample
(
    input rstn,
    input clk1,
    input [31:0] din,
    input din_en,

    input clk2,
    output [31:0] dout,
    output dout_en
);

    // 4-stage registers, 3-stage for clap sync, 1-stage for edge detection
    reg [3:0] edge_r;
    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            edge_r <= 4'b0;
        end
        else begin
            edge_r <= {edge_r[2:0], clk1};
        end
    end
    
    wire edge_pos;
    assign edge_pos = edge_r[2] & ~edge_r[3];

    // delay counter, detect slow clk posedge then start count
    reg [5:0] cnt;
    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            cnt <= 6'h3f;
        end
        else if (edge_pos & din_en) begin
            cnt <= 6'h0;
        end
        else if (cnt != 6'h3f) begin
            cnt <= cnt + 1'b1;
        end
    end

    // data
    reg [31:0] dout_r;
    reg dout_en_r;
    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            dout_r <= 32'b0;
        end
        else if (din_en && cnt == 47) begin // slow clk middle
            dout_r <= din;
        end
    end

    // data_en delay one cycle compare with data
    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            dout_en_r <= 1'b0;
        end
        else if (din_en && cnt == 48) begin
            dout_en_r <= 1'b1;
        end
        else begin
            dout_en_r <= 1'b0;
        end
    end

    assign dout = dout_r;
    assign dout_en = dout_en_r;

endmodule
