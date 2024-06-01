// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/01 14:53
// Last Modified : 2024/06/01 15:00
// File Name     : slow2fast_1.v
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
module slow2fast_1
(
    input rstn,
    input clk1,
    input clk2,
    output sig2
);

    wire sig1;

    slow_domain_1 u_slow_domain_1
    (
        .clk1(clk1),
        .rstn(rstn),
        .sig1(sig1)
    );

    fast_domain_1 u_fast_domain_1
    (
        .clk1(clk1),
        .sig1(sig1),
        .rstn(rstn),
        .clk2(clk2),
        .sig2(sig2)
    );

endmodule
