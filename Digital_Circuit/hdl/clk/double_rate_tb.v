// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/07/06 16:55
// Last Modified : 2024/07/06 17:44
// File Name     : double_rate_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/07/06   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module double_rate_tb;

    reg clk_100mhz, clk_200mhz;
    reg rstn;
    reg csn;
    reg [7:0] din;
    reg din_en;
    wire [7:0] dout;
    wire dout_en;

    always #(2.5) clk_200mhz = ~clk_200mhz;
    always @ (posedge clk_200mhz) clk_100mhz = ~clk_100mhz;

    initial begin
        clk_100mhz = 1'b0;
        clk_200mhz = 1'b0;
        rstn = 1'b0;
        din = 8'b0;
        din_en = 1'b0;
        csn = 1'b0;
        #11 rstn = 1'b1;
        @(negedge clk_100mhz);
        din_en = 1'b1;
        #0.2;
        csn = 1'b1;
        forever begin
            @(posedge clk_100mhz);
            #0.2;
            csn = 1'b0;
            @(negedge clk_100mhz);
            #0.2;
            csn = 1'b1;
        end
    end

    always @ (negedge clk_200mhz) begin
        din <= {$random()} % 8'hFF;
    end

    double_rate u_double_rate
    (
        .rstn(rstn),
        .clk(clk_100mhz),
        .csn(csn),
        .din(din),
        .din_en(din_en),
        .dout(dout),
        .dout_en(dout_en)
    );

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

    initial begin
        $fsdbDumpfile("double_rate.fsdb");
        $fsdbDumpvars(0, double_rate_tb);
    end

endmodule
