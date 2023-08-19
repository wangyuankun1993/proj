// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : YuankunWang
// Email         : yuankun.wang@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/02/02 00:15
// Last Modified : 2023/08/20 00:46
// File Name     : full_adder1_tb.v
// Description   :
//         
// Copyright (c) 2023 Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/02/02   YuankunWang     1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module full_adder1_tb;
    reg Ai, Bi, Ci;
    wire So, Co;

    initial begin
        {Ai, Bi, Ci} = 3'b0;
        forever begin
            #10;
            {Ai, Bi, Ci} = {Ai, Bi, Ci} + 1'b1;
        end
    end

    full_adder1 u_full_adder1(
        .Ai(Ai),
        .Bi(Bi),
        .Ci(Ci),
        .So(So),
        .Co(Co)
    );

    initial begin
        $fsdbDumpfile("full_adder1.fsdb");
        $fsdbDumpvars(0, full_adder1_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000) begin
                $finish;
            end
        end
    end

endmodule
