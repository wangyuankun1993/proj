// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2023/09/01 00:42
// Last Modified : 2023/09/01 00:55
// File Name     : pad.v
// Description   :
//         
// Copyright (c) 2023 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2023/09/01   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module pad(
    input DIN, // pad driver when pad configured as output
    input OEN, // pad direction(1-input, 0-output)
    input [1:0] PULL, // pull function(00,01-dispull, 10-pullup, 11-pulldown)
    inout PAD,
    output reg DOUT // pad load when pad configured as input
);

    // input: (not effect pad external input logic), output: DIN->PAD
    assign PAD = OEN ? 'bz : DIN;

    // input: (PAD->DOUT)
    always @ (*) begin
        if (OEN == 1) begin
            DOUT = PAD;
        end
        else begin
            DOUT = 'bz;
        end
    end

    // use tristate gate in Verilog to realize pull up/down function
    bufif1 puller(PAD, PULL[0], PULL[1]);

endmodule
