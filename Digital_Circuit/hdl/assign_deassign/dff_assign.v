// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/08/30 00:41
// Last Modified : 2023/08/30 00:45
// File Name     : dff_assign.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/08/30   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module dff_assign(
    input rstn,
    input clk,
    input D,
    output reg Q
);

    always @ (posedge clk) begin
        Q <= D;
    end

    always @ (negedge rstn) begin
        if (!rstn) begin
            assign Q = 1'b0;
        end
        else begin
            deassign Q;
        end
    end

endmodule
