// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/05/26 18:26
// Last Modified : 2024/05/26 18:28
// File Name     : top.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/05/26   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module top
(
    output and_out,
    input in1, in2, clk
);

    wire res_tmp;
    and_gate u_and_gate(res_tmp, in1, in2);
    d_gate u_d_gate(and_out, res_tmp, clk);

endmodule
