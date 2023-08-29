// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/08/27 23:37
// Last Modified : 2023/08/29 00:16
// File Name     : repeat_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/08/27   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module repeat_tb;

    reg [3:0] counter;
    initial begin
        counter = 4'b0;
        repeat (11) begin
            #10;
            counter = counter + 1'b1;
        end
    end
    
    reg clk;
    reg rstn;
    reg enable;
    reg [3:0] buffer [7:0];
    integer j;

    initial begin
        clk = 1'b0;
        rstn = 1'b1;
        enable = 1'b0;
        #3;
        rstn = 1'b0;
        #3;
        rstn = 1'b1;
        enable = 1'b1;
        forever begin
            clk = ~clk;
            #5;
        end
    end

    always @ (posedge clk or negedge rstn) begin
        j = 0;
        if (!rstn) begin
            repeat (8) begin
                buffer[j] = 4'b0;
                j = j + 1;
            end
        end
        else if (enable) begin
            repeat (8) begin
                @(posedge clk) buffer[j] = counter;
                j = j + 1;
            end
        end
    end

    initial begin
        $fsdbDumpfile("repeat.fsdb");
        $fsdbDumpvars(0, repeat_tb);
    end

    always begin
        #10;
        if ($time >= 1000)
            $finish;
    end

endmodule
