// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/10 19:10
// Last Modified : 2024/06/10 19:36
// File Name     : pulse_sync_fast2slow_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/06/10   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module pulse_sync_fast2slow_tb;

    reg clk_100mhz;
    reg clk_25mhz;
    reg rstn;

    initial begin
        clk_100mhz = 1'b0;
        clk_25mhz = 1'b0;
        rstn = 1'b0;
        #11;
        rstn = 1'b1;
    end
    always #5 clk_100mhz = ~clk_100mhz;
    always #20 clk_25mhz = ~clk_25mhz;

    reg [7:0] cnt;
    reg pulse_sig;
    always @ (posedge clk_100mhz or negedge rstn) begin
        if (~rstn) begin
            cnt <= 8'b0;
        end
        else begin
            cnt <= cnt + 1'b1;
        end
    end

    // generate pulse
    always @ (posedge clk_100mhz or negedge rstn) begin
        if (~rstn) begin
            pulse_sig <= 1'b0;
        end
        else if (cnt == 5 || cnt == 40 || cnt == 42 || cnt >=75 && cnt <= 81 || cnt == 85 || cnt == 87) begin
            pulse_sig <= 1'b1;
        end
        else begin
            pulse_sig <= 1'b0;
        end
    end

    pulse_sync_fast2slow u_pulse_sync_fast2slow
    (
        .rstn(rstn),
        .clk_fast(clk_100mhz),
        .pulse_fast(pulse_sig),
        .clk_slow(clk_25mhz),
        .pulse_slow()
    );

    initial begin
        $fsdbDumpfile("pulse_sync_fast2slow.fsdb");
        $fsdbDumpvars(0, pulse_sync_fast2slow_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

endmodule
