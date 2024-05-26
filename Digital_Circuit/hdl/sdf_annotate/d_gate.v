// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/05/26 18:16
// Last Modified : 2024/05/26 18:26
// File Name     : d_gate.v
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
module d_gate
(
    output Q,
    input D, CP
);

    reg Q_r;
    always @ (posedge CP)
        Q_r <= D;
    assign Q = Q_r;

    specify
        if (D == 1'b1)
            (posedge CP => (Q +: D)) = (1.3:1.5:1.7, 1.1:1.4:1.9);
        if (D == 1'b0)
            (posedge CP => (Q +: D)) = (1.2:1.4:1.6, 1.0:1.3:1.8);
        $setup(D, posedge CP, 1);
    endspecify

endmodule
