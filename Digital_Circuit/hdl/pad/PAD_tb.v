// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/03/16 11:47
// Last Modified : 2024/03/17 18:58
// File Name     : PAD_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/03/16   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module PAD_tb;

    parameter PULL_UP = 1;
    parameter PULL_DOWN = 0;
    parameter IO0_OUT = 0;
    parameter IO1_OUT = 1;
    parameter IO2_OUT = 2;
    parameter IO3_OUT = 3;
    parameter IO0_IN = 0;
    parameter IO1_IN = 1;
    parameter IO2_IN = 2;
    parameter IO3_IN = 3;
    reg [3:0] DIN, OEN;
    wire [3:0] DOUT;
    wire [3:0] PAD;

    // test connection control, using tranif1
    reg [1:0] con_ena;
    tranif1 tr0 (PAD[0], PAD[1], con_ena[0]);
    tranif1 tr1 (PAD[2], PAD[3], con_ena[1]);
    reg err = 0;

    task test_io_conn;
        // test pull
        input pull_type;
        // test conn
        input [1:0] xout;
        input [1:0] yin;
        DIN[xout] = ~pull_type;
        #20;
        if (DOUT[yin] != ~pull_type) begin
            $display("write value and get value is: %h, %h", ~pull_type, DOUT[yin]);
            err |= 1;
        end
        DIN[xout] = pull_type;
        #20;
        if (DOUT[yin] != pull_type) begin
            $display("write value and get_value is: %h, %h", pull_type, DOUT[yin]);
            err |= 1;
        end
    endtask

    initial begin
        con_ena = 2'b01;
        OEN = 4'b1111;
        #13;
        // test between io0/io1
        OEN[0] = 0;
        OEN[1] = 1; // gpio0 -> gpio1
        test_io_conn(PULL_UP, IO0_OUT, IO1_IN);
        OEN[0] = 1;
        OEN[1] = 0; // gpio0 -> gpio1
        test_io_conn(PULL_UP, IO1_OUT, IO0_IN);
        OEN = 4'b1111;
        con_ena = 2'b10;
        OEN[2] = 0;
        OEN[3] = 1;
        test_io_conn(PULL_DOWN, IO2_OUT, IO3_IN);
        OEN[2] = 1;
        OEN[3] = 0;
        test_io_conn(PULL_DOWN, IO3_OUT, IO2_IN);
    end

    PADUP u_PADUP0(DIN[0], OEN[0], PAD[0], DOUT[0]);
    PADUP u_PADUP1(DIN[1], OEN[1], PAD[1], DOUT[1]);
    PADDOWN u_PADDOWN2(DIN[2], OEN[2], PAD[2], DOUT[2]);
    PADDOWN u_PADDOWN3(DIN[3], OEN[3], PAD[3], DOUT[3]);
    
    initial begin
        $fsdbDumpfile("PAD.fsdb");
        $fsdbDumpvars(0, PAD_tb);
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
