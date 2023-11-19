// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/11/19 18:12
// Last Modified : 2023/11/19 23:46
// File Name     : competition_hazard_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/11/19   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps
module competition_hazard_tb;

    reg clk;
    reg rst_n;
    reg en;
    reg din_rvs;
    wire flag_safe, flag_dgs;

    // clock and rst_n generating
    initial begin
        rst_n = 1'b0;
        clk = 1'b0;
        #5 rst_n = 1'b1;
        forever begin
            #5 clk = ~clk;
        end
    end

    initial begin
        en = 1'b0;
        din_rvs = 1'b1;
        #19; en = 1'b1;
        #1; din_rvs = 1'b0;
    end
    
    clap_delay u_clap_delay(
        .clk(clk),
        .rst_n(rst_n),
        .en(en),
        .din_rvs(din_rvs),
        .flag(flag_dgs)
    );

    initial begin
        $fsdbDumpfile("clap_delay.fsdb");
        $fsdbDumpvars(competition_hazard_tb, 0);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 1000) $finish;
        end
    end

endmodule
