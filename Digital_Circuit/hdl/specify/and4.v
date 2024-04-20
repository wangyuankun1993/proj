// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/04/20 12:02
// Last Modified : 2024/04/20 12:23
// File Name     : and4.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/04/20   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module and4
(
    output out,
    input a, b, c, d
);

    specify
        specparam ab_2_out = 2.5;
        specparam cd_2_out = 3.5;

        //(a => out) = ab_2_out;
        //(b => out) = ab_2_out;
        //(c => out) = cd_2_out;
        //(d => out) = cd_2_out;
        (a,b *> out) = ab_2_out;
        (c,d *> out) = cd_2_out;

    endspecify

    wire an1, an2;
    and u_and1(an1, a, b);
    and u_and2(an2, c, d);
    and u_and3(out, an1, an2);

endmodule
