// ---------------------------------------------
// File Name       : testbench.v
// Author          : Yuankun.Wang
// Email           : wangyuankun@aliyun.com
// Created Time    : 2024-10-06 00:21:48
// Last Modified : 2024/10/06 18:39
// Description     : 
// ---------------------------------------------
`timescale 1ns/1ps

module testbench;

    reg clk;
    initial begin
        clk = 0;
    end
    always #5 clk = ~clk;

    // change timescale
    initial begin
        #10;
        $timeformat(-12, 5, " my-ps", 15);
    end
    initial begin
        #5;
        $printtimescale();
        $display("Time before resetup: %t", $time);
        #10;
        $printtimescale();
        $display("Time after resetup: %t", $time);
    end

    initial begin
        #10;
        $display("$time output1: %t", $time);
        $display("$stime output1: %t", $stime);
        $display("$realtime output1: %t", $realtime);
        #3.2;
        $display("$time output2: %t", $time);
        $display("$stime output2: %t", $stime);
        $display("$realtime output2: %t", $realtime);
        #5.6;
        $display("$time output3: %t", $time);
        $display("$stime output3: %t", $stime);
        $display("$realtime output3: %t", $realtime);
    end

    initial begin
        forever begin
            #100;
            //if ($time >= 10000) $finish(0);
            //if ($time >= 10000) $finish(1);
            if ($time >= 10000) $finish(2);
        end
    end

endmodule
