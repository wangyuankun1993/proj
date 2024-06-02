// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/02 12:03
// Last Modified : 2024/06/02 12:17
// File Name     : delay_clap.v
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
module delay_clap
(
    input clk, // async slow clk
    input sig1, // async signal

    input rstn,
    input clk2, // destination fast clk
    output sig2
);

    reg [2:0] sig2_r; // 3-stage registers
    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            sig2_r <= 3'b0;
        end
        else begin
            sig2_r <= {sig2_r[1:0], sig1};
        end
    end

    assign sig2 = sig2_r[1] & ~sig2_r[2];

endmodule
