// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/01 16:16
// Last Modified : 2024/06/01 16:36
// File Name     : fast_domain_2.v
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
module fast_domain_2
(
    input clk1,
    input rstn,
    output sig11
);

    reg [3:0] cnt;
    always @ (posedge clk1 or negedge rstn) begin
        if (~rstn) begin
            cnt <= 4'b0;
        end
        else begin
            cnt <= cnt + 1'b1;
        end
    end

    reg sig11_r;
    always @ (posedge clk1 or negedge rstn) begin
        if (~rstn) begin
            sig11_r <= 1'b0;
        end
        else if (cnt == 9) begin
            sig11_r <= 1'b1;
        end
        else begin
            sig11_r <= 1'b0;
        end
    end

    assign sig11 = sig11_r;

endmodule
