// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/08 00:32
// Last Modified : 2023/09/08 00:38
// File Name     : digital_tube.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/08   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module digital_tube(
    input clk,
    input rstn,
    input en,
    input [3:0] single_digit,
    input [3:0] ten_digit,
    input [3:0] hundred_digit,
    input [3:0] kilo_digit,
    output reg [3:0] csn, // chip select, low-available
    output reg [6:0] abcdefg // light control
);

    reg [2:0] scan_r; // scan_ctrl
    always @ (posedge clk or negedge rstn) begin
        if (!rstn) begin
            csn <= 4'b1111;
            abcdefg <= 7'b0;
            scan_r <= 3'b0;
        end
