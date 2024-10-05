// ---------------------------------------------
// File Name       : testbench.v
// Author          : Yuankun.Wang
// Email           : wangyuankun@aliyun.com
// Created Time    : 2024-10-05 17:28:06
// Last Modified : 2024/10/05 19:28
// Description     : 
// ---------------------------------------------
`timescale 1ns/1ps

module testbench;

    reg clk;
    initial begin
        clk = 0;
    end
    always #5 clk = ~clk;
    integer seed;
    initial begin
        seed = 2;
        #30;
        seed = 10;
    end
    reg [15:0] randnum_noseed;
    always @ (posedge clk) begin
        randnum_noseed <= $random();
    end
    reg [15:0] randnum_wtseed;
    always @ (posedge clk) begin
        randnum_wtseed <= $random(seed);
    end

    // with a range
    parameter MAX_NUM = 512;
    parameter MIN_NUM = 256;
    reg [15:0] num_range1, num_range2, num_range3;
    always @ (posedge clk) begin
        num_range1 <= $random() % MAX_NUM;
        num_range2 <= {$random()} % MAX_NUM;
        num_range3 <= MIN_NUM + {$random()} % (MAX_NUM-MIN_NUM+1);
    end

    integer seed_dis;
    initial seed_dis = 0;
    // uniform distribution
    reg [15:0] data_uniform;
    always @ (posedge clk) begin
        data_uniform <= $dist_uniform(seed_dis, MIN_NUM, MAX_NUM);
    end

    // normal distribution
    reg [15:0] data_normal;
    always @ (posedge clk) begin
        data_normal <= $dist_normal(seed_dis, 0, 1);
    end

    // poisson distribution
    reg [15:0] data_poisson;
    always @ (posedge clk) begin
        data_poisson <= $dist_poisson(seed_dis, 4);
    end

    // exponential distribution
    reg [15:0] data_exp;
    always @ (posedge clk) begin
        data_exp <= $dist_exponential(seed_dis, 1);
    end

    // chi-square distribution
    reg [15:0] data_chi_sq;
    always @ (posedge clk) begin
        data_chi_sq <= $dist_chi_square(seed_dis, 6);
    end

    // t distribution
    reg [15:0] data_t;
    always @ (posedge clk) begin
        data_t <= $dist_t(seed_dis, 5);
    end

    // Erlang distribution
    reg [15:0] data_erlang;
    always @ (posedge clk) begin
        data_erlang <= $dist_erlang(seed_dis, 3, 6);
    end

    initial begin
        forever begin
            #100;
            if ($time >= 10000) $finish;
        end
    end

    initial begin
        $fsdbDumpfile("testbench.fsdb");
        $fsdbDumpvars(0, testbench);
    end

endmodule
