// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/03 00:36
// Last Modified : 2023/09/03 00:43
// File Name     : full_adder4.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/03   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module full_adder4(
    input [3:0] a, // adder1
    input [3:0] b, // adder2
    input c, // input carry bit
    output [3:0] so, // adding result
    output co // output carry bit
);

    wire [3:0] co_temp;
    full_adder1 u_adder0(
        .Ai(a[0]),
        .Bi(b[0]),
        .Ci(c==1'b1 ? 1'b1 : 1'b0),
        .So(so[0]),
        .Co(co_temp[0])
    );

    genvar i;
    generate
        for (i=1;i<=3;i=i+1) begin: adder_gen
            full_adder1 u_adder(
                .Ai(a[i]),
                .Bi(b[i]),
                .Ci(co_temp[i-1]),
                .So(so[i]),
                .Co(co_temp[i])
            );
        end
    endgenerate

    assign co = co_temp[3];
    
endmodule
