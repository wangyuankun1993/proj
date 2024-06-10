// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/06/10 18:01
// Last Modified : 2024/06/10 19:10
// File Name     : pulse_sync_fast2slow.v
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
module pulse_sync_fast2slow
#(
    parameter PULSE_INIT = 1'b0
)
(
    input rstn,
    input clk_fast,
    input pulse_fast,
    input clk_slow,
    output pulse_slow
);

    wire clear_n;
    reg pulse_fast_r;

    /*****************fast clk*****************/
    //(1) When detect the pulse, doesn't need pull down the pulse
    always @ (posedge clk_fast or negedge rstn) begin
        if (~rstn) begin
            pulse_fast_r <= PULSE_INIT;
        end
        else if (~clear_n) begin
            pulse_fast_r <= 1'b0;
        end
        else if (pulse_fast) begin
            pulse_fast_r <= 1'b1;
        end
    end

    reg [1:0] pulse_fast2slow_r;
    /*****************slow clk*****************/
    //(2) Slow clk delay clap capture pulse
    always @ (posedge clk_slow or negedge rstn) begin
        if (~rstn) begin
            pulse_fast2slow_r <= 2'b0;
        end
        else begin
            pulse_fast2slow_r <= {pulse_fast2slow_r[0], pulse_fast_r};
        end
    end
    assign pulse_slow = pulse_fast2slow_r[1];

    reg [1:0] pulse_slow2fast_r;
    /*****************feedback from slow clk to fast clk*****************/
    //(3) delay clap capture feedback signal
    always @ (posedge clk_fast or negedge rstn) begin
        if (~rstn) begin
            pulse_slow2fast_r <= 2'b0;
        end
        else begin
            pulse_slow2fast_r <= {pulse_slow2fast_r[0], pulse_slow};
        end
    end
    //control fast domain pulse pull down
    assign clear_n = ~(~pulse_fast & pulse_slow2fast_r[1]);

endmodule
