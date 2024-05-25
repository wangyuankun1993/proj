// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/05/24 22:09
// Last Modified : 2024/05/24 22:19
// File Name     : full_adder8.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/05/24   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module full_adder8
(
    input [7:0] a, // adder1
    input [7:0] b, // adder2
    input c, // input carry bit
    output [7:0] so, // adding result
    output co // output carry bit
);

    wire [7:0] co_temp;

    full_adder1 u_full_adder1_0
    (
        .Ai(a[0]),
        .Bi(b[0]),
        .Ci(c==1'b1 ? 1'b1 : 1'b0),
        .So(so[0]),
        .Co(co_temp[0])
    );

    genvar i;
    generate
        for (i=1; i<=7; i=i+1) begin: adder_gen
            full_adder1 u_full_adder1
            (
                .Ai(a[i]),
                .Bi(b[i]),
                .Ci(co_temp[i-1]),
                .So(so[i]),
                .Co(co_temp[i])
            );
        end
    endgenerate

    assign co = co_temp[7];

endmodule
