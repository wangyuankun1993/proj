// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/11/19 20:22
// Last Modified : 2023/11/19 23:50
// File Name     : clap_delay.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/11/19   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module clap_delay(
    input clk,
    input rst_n,
    input en,
    input din_rvs,
    output reg flag
);
    reg din_rvs_r;
    reg en_r;

    always @ (posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            din_rvs_r <= 1'b0;
            en_r <= 1'b0;
        end
        else begin
            din_rvs_r <= din_rvs;
            en_r <= en;
        end
    end

    wire condition = din_rvs_r & en_r;

    always @ (posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            flag <= 1'b0;
        end 
        else begin
            flag <= condition;
        end
    end

endmodule
