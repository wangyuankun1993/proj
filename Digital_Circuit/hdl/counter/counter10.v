// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : YuankunWang
// Email         : yuankun.wang@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/01/01 23:21
// Last Modified : 2023/01/02 18:34
// File Name     : counter10.v
// Description   :
//         
// Copyright (c) 2023 Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/01/01   YuankunWang     1.0                     Original
// -FHDR----------------------------------------------------------------------------
module counter10(
    output [3:0] cnt,
    output cout,
    input rstn,
    input clk
);

    reg [3:0] cnt_temp;
    always @ (posedge clk or negedge rstn) begin
        if (!rstn) begin
            cnt_temp <= 4'b0;
        end
        else if (cnt_temp == 4'b1001) begin
            cnt_temp <= 4'b0;
        end
        else begin
            cnt_temp <= cnt_temp + 4'b1;
        end
    end

    assign cout = (cnt_temp == 4'b1001);
    assign cnt = cnt_temp;
endmodule
