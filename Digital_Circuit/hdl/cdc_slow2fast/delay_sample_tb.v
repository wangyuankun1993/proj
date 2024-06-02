// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/02 15:25
// Last Modified : 2024/06/02 15:39
// File Name     : delay_sample_tb.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/06/02   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module delay_sample_tb;

    reg clk_100mhz;
    reg clk_20mhz;
    reg clk_999khz;
    reg rstn;
    reg [31:0] din;
    reg din_en;

    initial begin
        clk_100mhz = 1'b0;
        clk_20mhz = 1'b0;
        clk_999khz = 1'b0;
        rstn = 1'b0;
        #11;
        rstn = 1'b1;
    end

    always #5 clk_100mhz = ~clk_100mhz;
    always #25 clk_20mhz = ~clk_20mhz;
    always #(1001/2) clk_999khz = ~clk_999khz;

    always @ (posedge clk_20mhz or negedge rstn) begin
        if (~rstn) begin
            din <= 32'h5555_aaaa;
            din_en <= 1'b0;
        end
        else begin
            din <= din + 32'h4321;
            din_en <= ~din_en;
        end
    end

    delay_sample u_delay_sample
    (
        .rstn(rstn),
        .clk1(clk_20mhz),
        .din(din),
        .din_en(din_en),
        .clk2(clk_100mhz),
        .dout(),
        .dout_en()
    );

    initial begin
        $fsdbDumpfile("delay_sample.fsdb");
        $fsdbDumpvars(0, delay_sample_tb);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

endmodule
