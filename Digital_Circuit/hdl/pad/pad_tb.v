// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/02 00:33
// Last Modified : 2023/09/02 00:42
// File Name     : pad_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/02   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module pad_tb;
    reg DIN, OEN;
    reg [1:0] PULL;
    wire PAD;
    wire DOUT;

    reg PAD_REG;
    assign PAD = OEN ? PAD_REG : 1'bz;

    initial begin
        PAD_REG = 1'bz; // pad with no dirve at first
        OEN = 1'b1; // input simulation
        #0; PULL = 2'b10; // pull down
        #20; PULL = 2'b11; // pull up
        #20; PULL = 2'b00; // dispull
        #20; PAD_REG = 1'b0;
        #20; PAD_REG = 1'b1;

        #30; OEN = 1'b0; // output simulation
             DIN = 1'bz;
        #15; DIN = 1'b0;
        #15; DIN = 1'b1;
    end

    pad u_pad(
        .DIN(DIN),
        .OEN(OEN),
        .PULL(PULL),
        .PAD(PAD),
        .DOUT(DOUT)
    );

    initial begin
        $fsdbDumpfile("pad.fsdb");
        $fsdbDumpvars(0, pad_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000)
                $finish;
        end
    end

endmodule
