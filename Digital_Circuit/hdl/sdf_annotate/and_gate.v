// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/05/26 17:52
// Last Modified : 2024/05/26 18:16
// File Name     : and_gate.v
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
module and_gate
(
    output Z,
    input A, B
);

    assign Z = A & B;

    specify
        specparam t_rise = 1.3:1.5:1.7;
        specparam t_fall = 1.1:1.3:1.6;
        (A, B *> Z) = (t_rise, t_fall);
    endspecify

endmodule
