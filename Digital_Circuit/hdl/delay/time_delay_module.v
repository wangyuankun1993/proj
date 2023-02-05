// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : YuankunWang
// Email         : yuankun.wang@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/02/05 16:07
// Last Modified : 2023/02/05 16:19
// File Name     : time_delay_module.v
// Description   :
//         
// Copyright (c) 2023 Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/02/05   YuankunWang     1.0                     Original
// -FHDR----------------------------------------------------------------------------
module time_delay_module(
    input ai, bi,
    output so_lose, so_get, so_normal
);
    assign #20 so_lose = ai & bi;
    assign #5  so_get  = ai & bi;
    assign     so_normal = ai & bi;

endmodule
