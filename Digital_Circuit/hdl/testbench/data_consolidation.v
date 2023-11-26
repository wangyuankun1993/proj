// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/11/26 23:36
// Last Modified : 2023/11/26 23:45
// File Name     : data_consolidation.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/11/26   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module data_consolidation
    (
        input clk,
        input rst_n,
        input [1:0] din,
        input din_en,
        output [7:0] dout,
        output dout_en
    );

    reg [7:0] data_r;
    reg [1:0] state_cnt;
    always @ (posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            state_cnt <= 2'b0;
            data_r <= 8'b0;
        end
        else if (din_en) begin
            state_cnt <= state_cnt + 1'b1;
            data_r <= {data_r[5:0], din};
        end
        else begin
            state_cnt <= 2'b0;
        end
    end
    assign dout = data_r;

    reg dout_en_r;
    always @ (posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            dout_en_r <= 1'b0;
        end
        else if (state_cnt == 2'd3 & din_en) begin
            dout_en_r <= 1'b1;
        end
        else begin
            dout_en_r <= 1'b0
        end
    end
    assign dout_en = dout_en_r;

endmodule
