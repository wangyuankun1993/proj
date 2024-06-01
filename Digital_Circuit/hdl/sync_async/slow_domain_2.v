// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/01 16:37
// Last Modified : 2024/06/01 16:50
// File Name     : slow_domain_2.v
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
module slow_domain_2
(
    input clk1,
    input sig11,
    input rstn,
    input clk2,
    output sig22
);

    reg [1:0] sig11_r;
    always @ (posedge clk1 or negedge rstn) begin
        if (~rstn) begin
            sig11_r <= 2'b0;
        end
        else begin
            sig11_r <= {sig11_r[0], sig11};
        end
    end

    reg sig22_r;
    always @ (posedge clk2 or negedge rstn) begin
        if (~rstn) begin
            sig22_r <= 1'b0;
        end
        else begin
            sig22_r <= |sig11_r;
        end
    end
    assign sig22 = sig22_r;

endmodule
