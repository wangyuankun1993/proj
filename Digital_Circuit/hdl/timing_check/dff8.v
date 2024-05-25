// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/05/25 10:39
// Last Modified : 2024/05/25 10:42
// File Name     : dff8.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/05/25   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module dff8
(
    input [7:0] d,
    input clk,
    output reg [7:0] q
);

    always @ (posedge clk)
        q <= d;
    specify
        $setup(d, posedge clk, 2);
        $hold(posedge clk, d, 3);
        (d, clk *> q) = 0.3;
    endspecify

endmodule
