// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/08/25 23:59
// Last Modified : 2023/08/26 00:02
// File Name     : mux4_1_case.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/08/25   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module mux4_1_case(
    input [1:0] sel,
    input [1:0] p0,
    input [1:0] p1,
    input [1:0] p2,
    input [1:0] p3,
    output [1:0] sout
);
    
    reg [1:0] sout_t;
    always @ (*)
        case(sel)
            2'b00: sout_t = p0;
            2'b01: sout_t = p1;
            2'b10: sout_t = p2;
            default: sout_t = p3;
        endcase
    assign sout = sout_t;

endmodule
