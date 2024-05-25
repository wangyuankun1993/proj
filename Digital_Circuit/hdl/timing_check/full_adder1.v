// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/05/24 22:05
// Last Modified : 2024/05/24 22:08
// File Name     : full_adder1.v
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
module full_adder1
(
    input Ai, Bi, Ci,
    output So, Co
);

    assign So = Ai ^ Bi ^ Ci;
    assign Co = (Ai & Bi) | (Ci & (Ai | Bi));

    specify
        (Ai, Bi, Ci *> So) = 1.1;
        (Ai, Bi *> Co) = 1.3;
        (Ci => Co) = 1.2;
    endspecify

endmodule
