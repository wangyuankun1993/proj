// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : YuankunWang
// Email         : yuankun.wang@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/02/05 16:12
// Last Modified : 2023/02/05 16:19
// File Name     : time_delay_module_tb.v
// Description   :
//         
// Copyright (c) 2023 Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/02/05   YuankunWang     1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module time_delay_module_tb;
    reg ai, bi;
    wire so_lose, so_get, so_normal;

    initial begin
        ai = 0;
        #25; ai = 1;
        #35; ai = 0; // 60ns
        #40; ai = 1; // 100ns
        #10; ai = 0; // 110ns
    end

    initial begin
        bi = 1;
        #70; bi = 0;
        #20; bi = 1;
    end

    time_delay_module u_time_delay_module(
        .ai(ai),
        .bi(bi),
        .so_lose(so_lose),
        .so_get(so_get),
        .so_normal(so_normal)
    );

    initial begin
        $dumpfile("time_delay_module_wave.vcd");
        $dumpvars(0, time_delay_module_tb);
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
