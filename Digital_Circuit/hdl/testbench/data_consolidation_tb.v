// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/11/28 22:45
// Last Modified : 2023/12/31 23:10
// File Name     : data_consolidation_tb.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/11/28   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
`timescale 1ns/1ps

module data_consolidation_tb;

    // signals declaration
    reg clk;
    reg rst_n;
    reg [1:0] din;
    reg din_en;
    wire [7:0] dout;
    wire dout_en;

    // clock generating
    real CYCLE_200MHz = 5;
    always begin
        clk = 0; #(CYCLE_200MHz/2);
        clk = 1; #(CYCLE_200MHz/2);
    end

    // reset generating
    initial begin
        rst_n = 1'b0;
        #8 rst_n = 1'b1;
    end

    // motivation
    int fd_rd;
    reg [7:0] data_in_temp; // for self check
    reg [15:0] read_temp; // 16 bit ascii data
    initial begin
        din_en = 1'b0;
        din = 2'b0;
        open_file("../../verification/testbench/data_in.dat", "r", fd_rd);
        wait (rst_n)
        #CYCLE_200MHz;

        // read data from file
        while (! $feof(fd_rd)) begin
            @(negedge clk);
            $fread(read_temp, fd_rd);
            din = read_temp[9:8];
            data_in_temp = {data_in_temp[5:0], din};
            din_en = 1'b1;
        end

        // stop data
        @(posedge clk);
        #2 din_en = 1'b0;
    end

    // open task
    task open_file;
        input string file_dir_name;
        input string rw;
        output int fd;

        fd = $fopen(file_dir_name, rw);
        if (!fd) begin
            $display("---iii---Failed to open file: %s", file_dir_name);
        end
        else begin
            $display("---iii---%s has been opened successfully.", file_dir_name);
        end
    endtask

    // module instantiation
    data_consolidation u_data_consolidation
    (
        .clk(clk),
        .rst_n(rst_n),
        .din(din),
        .din_en(din_en),
        .dout(dout),
        .dout_en(dout_en)
    );

    // auto check
    reg [7:0] err_cnt;
    int fd_wr;

    initial begin
        err_cnt = 8'b0;
        open_file("../../verification/testbench/data_out.dat", "w", fd_wr);
        forever begin
            @(negedge clk);
            if (dout_en) begin
                $fdisplay(fd_wr, "%h", dout);
            end
        end
    end
    
    always @ (posedge clk) begin
        #1;
        if (dout_en) begin
            if (data_in_temp != dout) begin
                err_cnt = err_cnt + 1'b1;
            end
        end
    end

    // simulation finish
    always begin
        #100;
        if ($time >= 10000) begin
            if (!err_cnt) begin
                $display("--------------------------------------");
                $display("Data process if OK!!!");
                $display("--------------------------------------");
            end
            else begin
                $display("--------------------------------------");
                $display("Error occurs in data process!!!");
                $display("--------------------------------------");
            end
            #1;
            $finish;
        end
    end

    // wave generating
    initial begin
        $fsdbDumpfile("data_consolidation.fsdb");
        $fsdbDumpvars(0, data_consolidation_tb);
    end

endmodule
