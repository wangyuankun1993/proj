// ---------------------------------------------
// File Name       : testbench.v
// Author          : Yuankun.Wang
// Email           : wangyuankun@aliyun.com
// Created Time    : 2024-10-07 14:58:07
// Last Modified : 2024/10/07 14:59
// Description     : 
// ---------------------------------------------
`timescale 1ns/1ps

module testbench;

    initial begin
        #10;
        $hello_runoob;
    end

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

endmodule
