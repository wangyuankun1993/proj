// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/01 17:02
// Last Modified : 2024/06/01 17:08
// File Name     : fast2slow_2.v
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
module fast2slow_2
(
    input rstn,
    input clk1,
    input clk2,
    output sig22
);

    wire sig11;

    fast_domain_2 u_fast_domain_2
    (
        .clk1(clk1),
        .rstn(rstn),
        .sig11(sig11)
    );

    slow_domain_2 u_slow_domain_2
    (
        .rstn(rstn),
        .clk1(clk1),
        .sig11(sig11),
        .clk2(clk2),
        .sig22(sig22)
    );

endmodule
