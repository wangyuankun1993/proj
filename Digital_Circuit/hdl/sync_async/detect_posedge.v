// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/05/29 22:01
// Last Modified : 2024/05/29 22:16
// File Name     : detect_posedge.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/05/29   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module detect_posedge
(
    output q,
    input clk,
    input rstn,
    input d
);

    reg [1:0] tmp_r;

    always @ (posedge clk or negedge rstn) begin
        if (~rstn) begin
            tmp_r <= 2'b0;
        end
        else begin
            tmp_r <= {tmp_r[0], d};
        end
    end
    assign pos_flag = tmp_r[0] & !tmp_r[1];

endmodule
