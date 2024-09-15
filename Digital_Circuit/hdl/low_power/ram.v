// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/09/15 14:05
// Last Modified : 2024/09/15 15:14
// File Name     : ram.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/09/15   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module ram
#(
    parameter AW = 2,
    parameter DW = 3
)
(
    input CLK,
    input [AW-1:0] A,
    input [DW-1:0] D,
    input EN,
    input WR, // i for write and 0 for read
    output reg [DW-1:0] Q
);

    parameter MASK = 3;

    reg [DW-1:0] mem [0:(1<<AW)-1];
    always @ (posedge CLK) begin
        if (EN & WR) begin
            mem[A] = D;
        end
        else if (EN & !WR) begin
            Q = mem[A];
        end
    end
endmodule
