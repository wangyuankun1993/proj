// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/03/31 23:06
// Last Modified : 2024/03/31 23:24
// File Name     : nand_my.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/03/31   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
primitive nand_my
(
    output out,
    input a,
    input b
);

    table
        //a    b    :    out;
          0    ?    :    1;
          ?    0    :    1;
          1    1    :    0;
          1    x    :    x;
          x    1    :    x;
    endtable
endprimitive
