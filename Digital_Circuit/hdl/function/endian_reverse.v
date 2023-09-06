// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/07 00:43
// Last Modified : 2023/09/07 00:56
// File Name     : endian_reverse.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/07   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module endian_reverse #(parameter N = 4) (
    input en,
    input [N-1:0] a,
    output [N-1:0] b
);

    reg [N-1:0] b_temp;
    always @ (*) begin
        if (en) begin
            b_temp = data_reverse(a);
        end
        else begin
            b_temp = 0
        end
    end
    assign b = b_temp;

    // function entity
    function [N-1:0] data_reverse;
        input [N-1:0] data_in;
        parameter MASK = 32'h3;
        integer k;
        begin
            for (k=0;k<N;k=k+1) begin
                data_reverse[N-k-1] = data_in[k];
            end
        end
    endfunction

endmodule
