// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/01 14:48
// Last Modified : 2024/06/01 14:53
// File Name     : fast_domain_1.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/06/01   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module fast_domain_1
(
    input clk1,
    input sig1,
    input rstn,
    input clk2,
    output sig2
);

    reg [1:0] sig2_r;

    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            sig2_r <= 2'b0;
        end
        else begin
            sig2_r <= {sig2_r[0], sig1};
        end
    end

    assign sig2 = sig2_r[0] & ~sig2_r[1];

endmodule
