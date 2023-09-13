// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/12 00:38
// Last Modified : 2023/09/14 00:41
// File Name     : xor_oper.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/12   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module xor_oper #(parameter N = 4) (
    input clk,
    input rstn,
    input [N-1:0] a,
    input [N-1:0] b,
    output [N-1:0] co
);

    reg [N-1:0] co_t;
    always @ (*) begin
        xor_oper_iner(a, b, co_t);
    end

    reg [N-1:0] co_r;
    always @ (posedge clk or negedge rstn) begin
        if (!rstn) begin
            co_r <= 'b0;
        end
        else begin
            co_r <= co_t;
        end
    end
    assign co = co_r;

    /*---------------- task ------------------*/
    task xor_oper_iner;
        input [N-1:0] numa;
        input [N-1:0] numb;
        output [N-1:0] numco;
        #3 numco = numa ^ numb;
    endtask

endmodule
