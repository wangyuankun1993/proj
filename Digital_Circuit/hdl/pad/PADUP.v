// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/03/16 11:37
// Last Modified : 2024/03/16 11:46
// File Name     : PADUP.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/03/16   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module PADUP(
    // DIN, pad driver when pad configured as output
    // OEN, pad direction(1-input, 0-output)
    input DIN, OEN,
    inout PAD,
    // pad load when pad configured as input
    output DOUT
);

    // input: not effect pad external input logic, output: DIN->PAD
    bufif0(PAD, DIN, OEN); // 0-output
    bufif1(DOUT, PAD, OEN); // 1-input
    pullup pu1 (PAD);

endmodule
