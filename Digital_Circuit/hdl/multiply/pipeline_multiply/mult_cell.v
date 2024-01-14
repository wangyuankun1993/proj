// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/01/14 23:04
// Last Modified : 2024/01/14 23:39
// File Name     : mult_cell.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/01/14   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module mult_cell #(parameter N=4, parameter M=4)
    (
        input clk,
        input rst_n,
        input en,
        input [M+N-1:0] mult1, // multiplicand
        input [M-1:0] mult2, // multiplier
        input [M+N-1:0] mult1_acci, // last accumulation result

        output reg [M+N-1:0] mult1_o, // multiplicand shift register
        output reg [M-1:0] mult2_shift, // multiplier shift register
        output reg [M+N-1:0] mult1_acco, // current accumulation result
        output reg ready
    );

    always @ ()
