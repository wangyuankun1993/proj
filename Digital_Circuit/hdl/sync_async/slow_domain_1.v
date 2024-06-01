// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/01 14:40
// Last Modified : 2024/06/01 14:44
// File Name     : slow_domain_1.v
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
module slow_domain_1
(
    input clk1,
    input rstn,
    output sig1
);

    reg [3:0] cnt;
    always @ (posedge clk1 or negedge rstn) begin
        if (~rstn) begin
            cnt <= 'b0;
        end
        else begin
            cnt <= cnt + 1'b1;
        end
    end

    reg sig1_r;
    always @ (posedge clk1 or negedge rstn) begin
        if (~rstn) begin
            sig1_r <= 1'b0;
        end
        else if (cnt == 9) begin
            sig1_r <= 1'b1;
        end
        else begin
            sig1_r <= 1'b0;
        end
    end
    assign sig1 = sig1_r;

endmodule
