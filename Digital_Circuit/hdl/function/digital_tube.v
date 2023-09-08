// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/08 00:32
// Last Modified : 2023/09/09 00:40
// File Name     : digital_tube.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/08   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module digital_tube(
    input clk,
    input rstn,
    input en,
    input [3:0] single_digit,
    input [3:0] ten_digit,
    input [3:0] hundred_digit,
    input [3:0] kilo_digit,
    output reg [3:0] csn, // chip select, low-available
    output reg [6:0] abcdefg // light control
);

    reg [1:0] scan_r; // scan_ctrl
    always @ (posedge clk or negedge rstn) begin
        if (!rstn) begin
            csn <= 4'b1111;
            abcdefg <= 7'b0;
            scan_r <= 2'b0;
        end
        else if (en) begin
            case(scan_r)
                2'd0: begin
                    scan_r <= 2'd1;
                    csn <= 4'b0111; // select single digit
                    abcdefg <= dt_translate(single_digit);
                end
                2'd1: begin
                    scan_r <= 2'd2;
                    csn <= 4'b1011; // select ten digit
                    abcdefg <= dt_translate(ten_digit);
                end
                2'd2: begin
                    scan_r <= 2'd3;
                    csn <= 4'b1101; // select hundred digit
                    abcdefg <= dt_translate(hundred_digit);
                end
                2'd3: begin
                    scan_r <= 2'd0;
                    csn <= 4'b1110; // select kilo digit
                    abcdefg <= dt_translate(kilo_digit);
                end
            endcase
        end
    end

    /*-------------- translate function --------------*/
    function [6:0] dt_translate;
        input [3:0] data;
        begin
            case(data)
                4'd0: dt_translate = 7'b111_1110; // number0
                4'd1: dt_translate = 7'b011_0000; // number1
                4'd2: dt_translate = 7'b110_1101; // number2
                4'd3: dt_translate = 7'b111_1001; // number3
                4'd4: dt_translate = 7'b011_0011; // number4
                4'd5: dt_translate = 7'b101_1011; // number5
                4'd6: dt_translate = 7'b101_1111; // number6
                4'd7: dt_translate = 7'b111_0000; // number7
                4'd8: dt_translate = 7'b111_1111; // number8
                4'd9: dt_translate = 7'b111_1011; // number9
            endcase
        end
    endfunction

endmodule

