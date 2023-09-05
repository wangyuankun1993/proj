// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/05 00:27
// Last Modified : 2023/09/06 00:22
// File Name     : ram_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/05   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module ram_tb;

    parameter AW = 4;
    parameter DW = 4;

    reg clk;
    reg [AW:0] a;
    reg [DW-1:0] d;
    reg en;
    reg wr;
    wire [DW-1:0] q;

    always begin
        #15; clk = 0;
        #15; clk = 1;
    end

    initial begin
        a = 10;
        d = 2;
        en = 1'b0;
        wr = 1'b0;
        repeat(10) begin
            @ (posedge clk);
            en = 1'b1;
            a = a + 1;
            wr = 1'b1;
            d = d + 1;
        end
        a = 10;
        repeat(10) begin
            @ (posedge clk);
            a = a + 1;
            wr = 1'b0;
        end
    end

    defparam u_ram_4x4.MASK = 7;
    ram_4x4 u_ram_4x4(
        .CLK(clk),
        .A(a[AW-1:0]),
        .D(d),
        .EN(en),
        .WR(wr),
        .Q(q)
    );

    initial begin
        $fsdbDumpfile("ram_tb.fsdb");
        $fsdbDumpvars(0, ram_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000)
                $finish;
        end
    end

endmodule
