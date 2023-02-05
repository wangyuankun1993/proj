// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : YuankunWang
// Email         : yuankun.wang@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/02/02 00:12
// Last Modified : 2023/02/02 00:14
// File Name     : full_adder1.v
// Description   :
//         
// Copyright (c) 2023 Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/02/02   YuankunWang     1.0                     Original
// -FHDR----------------------------------------------------------------------------
module full_adder1(
    input Ai, Bi, Ci,
    output So, Co
);

    assign So = Ai ^ Bi ^ Ci;
    assign Co = (Ai & Bi) | (Ci & (Ai | Bi));
endmodule
