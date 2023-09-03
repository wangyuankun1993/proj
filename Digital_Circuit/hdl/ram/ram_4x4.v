// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/04 00:13
// Last Modified : 2023/09/04 00:19
// File Name     : ram_4x4.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/04   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module ram_4x4(
    input CLK,
    input [3:0] A,
    input [3:0] D,
    input EN,
    input WR, // 1 for write and 0 for read
    output reg [3:0] Q
);

    parameter MASK = 3;

    reg [3:0] mem [0:7];
    always @ (posedge CLK) begin
        if (EN && WR) begin
            mem[A] <= D & MASK;
        end
        else if (EN && !WR) begin
            Q <= mem[A] & MASK;
        end
    end

endmodule
