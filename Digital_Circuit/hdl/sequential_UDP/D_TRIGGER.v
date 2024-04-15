// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/04/14 23:12
// Last Modified : 2024/04/15 23:28
// File Name     : D_TRIGGER.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/04/14   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
primitive D_TRIGGER
(
    output reg Q = 0,
    input RST, CP, D
);

    table
        // RST    CP    D    :Q    :Q+;
        // (1) clear
        1        ?     ?    :?    :0 ; // RST=1 clear
        (??)     ?     ?    :?    :- ; // ignore RST edge variation
        // (2) clk negedge capture
        0        (10)  0    :?    :0 ; // clk negedge capture
        0        (10)  1    :?    :1 ;
        // possible negedge
        0        (1x)  ?    :?    :- ; // possible negedge keep
        0        (x0)  ?    :?    :- ;
        // (3) clk posedge keep
        0        (0?)  ?    :?    :- ; // clk posedge keep
        // possbile posedge
        0        (x1)  ?    :?    :- ; // possible clk posedge keep
        // (4) not clk edge keep
        0        ?     (??) :?    :- ;
    endtable

endprimitive
