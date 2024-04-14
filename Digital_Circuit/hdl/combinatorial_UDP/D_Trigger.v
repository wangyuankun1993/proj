// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/03/24 21:30
// Last Modified : 2024/03/31 23:28
// File Name     : D_Trigger.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/03/24   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module D_Trigger
(
    input D,
    input CP,
    output Q,
    output QR
);


    // part1, not gate
    wire CPN, DN;
    not (CPN, CP);
    not (DN, D);

    // part2, master trigger
    wire G3O, G4O;
    nand_my (G3O, D, CP);
    nand_my (G4O, DN, CP);
    wire G1O, G2O;
    nand_my (G1O, G3O, G2O);
    nand_my (G2O, G4O, G1O);

    // part3, slave trigger
    wire G7O, G8O, G1ON;
    nand_my (G7O, G1O, CPN);
    not (G1ON, G1O);
    nand_my (G8O, G1ON, CPN);
    wire G5O, G6O;
    nand_my (G5O, G7O, G6O);
    nand_my (G6O, G8O, G5O);

    assign Q = G5O;
    assign QR = G6O;

endmodule
