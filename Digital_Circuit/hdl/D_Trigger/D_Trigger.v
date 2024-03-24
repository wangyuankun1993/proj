// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/03/24 21:30
// Last Modified : 2024/03/24 22:29
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

    parameter RISE_TIME = 0.11;
    parameter FALL_TIME = 0.07;

    // part1, not gate
    wire CPN, DN;
    not #(RISE_TIME, FALL_TIME) (CPN, CP);
    not #(RISE_TIME, FALL_TIME) (DN, D);

    // part2, master trigger
    wire G3O, G4O;
    nand #(RISE_TIME, FALL_TIME) (G3O, D, CP);
    nand #(RISE_TIME, FALL_TIME) (G4O, DN, CP);
    wire #(RISE_TIME, FALL_TIME) G1O, G2O;
    nand #(RISE_TIME, FALL_TIME) (G1O, G3O, G2O);
    nand #(RISE_TIME, FALL_TIME) (G2O, G4O, G1O);

    // part3, slave trigger
    wire G7O, G8O, G1ON;
    nand #(RISE_TIME, FALL_TIME) (G7O, G1O, CPN);
    not #(RISE_TIME, FALL_TIME) (G1ON, G1O);
    nand #(RISE_TIME, FALL_TIME) (G8O, G1ON, CPN);
    wire G5O, G6O;
    nand #(RISE_TIME, FALL_TIME) (G5O, G7O, G6O);
    nand #(RISE_TIME, FALL_TIME) (G6O, G8O, G5O);

    assign Q = G5O;
    assign QR = G6O;

endmodule
