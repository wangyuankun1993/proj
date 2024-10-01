// +FHDR----------------------------------------------------------------------------
// Project Name  : IC_Design
// Device        : Xilinx
// Author        : Yuankun.Wang
// Email         : wangyuankun@aliyun.com
// Website       : yuankun.wang
// Created On    : 2024/09/22 19:40
// Last Modified : 2024/10/01 13:19
// File Name     : testbench.v
// Description   :
//         
// Copyright (c) 2024 CIX Co.,Ltd..
// ALL RIGHTS RESERVED
// 
// ---------------------------------------------------------------------------------
// Modification History:
// Date         By              Version                 Change Description
// ---------------------------------------------------------------------------------
// 2024/09/22   Yuankun.Wang    1.0                     Original
// -FHDR----------------------------------------------------------------------------
module testbench;

    // open/close file
    integer fd1, fd2;
    integer err1, err2;
    reg [320:0] str1, str2;
    initial begin
        #10;
        // existing file
        fd1 = $fopen("DATA_RD.hex", "r");
        err1 = $ferror(fd1, str1);
        $display("File1 descriptor is: %h.", fd1);
        $display("Error1 number is: %h.", err1);
        $display("Error2 info is: %s.", str1);
        $fclose(fd1);
        // not existing file
        fd2 = $fopen("./FILE_NOEXIST.HEX", "r");
        err2 = $ferror(fd2, str2);
        $display("File2 descriptor is: %h.", fd2);
        $display("Error2 number is: %h.", err2);
        $display("Error2 info is: %s.", str2);
        $fclose(fd2);
    end

    // write file
    integer fd;
    integer err, str;
    initial begin
        fd = $fopen("./DATA_RD.hex", "a+");
        err = $ferror(fd, str);
        if (~err) begin
            $fdisplay(fd, "New data1: %h", fd);
            $fdisplay(fd, "New data2: %h", str);
            $fdisplay(fd, "New data3: %h", err);
        end
        $fclose(fd);
    end

    // write string
    reg [299:0] str_swrite, str_sformat;
    reg [63:0] str_buf;
    integer len, age;
    initial begin
        #20;
        str_buf = "runoob!";
        age = 9;

        // $swrite write string format contains variation
        $swrite(str_swrite, "%s age is %d", str_buf, age);
        $display("%s", str_swrite);
        // $swrite write string not contains variation
        $swrite(str_swrite, "years ", "old.");
        $display("%s", str_swrite);
        // $swrite write string with variation, not suggest
        $swrite(str_swrite, age);
        $display("$swrite err test: %s", str_swrite);
        $display();

        // $sformat write string format contains variation
        $sformat(str_sformat, "I have learnt in %s", str_buf);
        $display("%s", str_sformat);
        // $sformat write string not contains variation, obtain string length
        len = $sformat(str_sformat, "for 4 years!");
        $display("%s", str_sformat);
        $display("$sformat len: %d", len);
        // $sformat write much more string without any variation, not suggest
        $sformat(str_sformat, "for", "4", "years!");
        $display("$sformat err test: %s", str_sformat);
    end

    // read char
    integer i;
    reg [31:0] char_buf;
    initial begin
        #30;
        fd = $fopen("DATA_RD.hex", "r");
        $write("Read char: ");
        err = $ferror(fd, str);
        if (!err) begin
            for (i=0; i<13; i++) begin
                char_buf[7:0] = $fgetc(fd); // read per single character
                $write("%c", char_buf[7:0]); // print character
            end
            $write(".\n");
        end

        $ungetc("1", fd); // continuous write file buf 3 times
        $ungetc("2", fd);
        $ungetc("3", fd);
        char_buf[7:0] = $fgetc(fd); // read 3
        char_buf[15:8] = $fgetc(fd); // read 2
        char_buf[23:16] = $fgetc(fd); // read 1, read buffer end
        char_buf[31:24] = $fgetc(fd); // read a
        $display("Read char after $ungetc: %s", char_buf);
        $fclose(fd);
    end

    // read line
    integer code;
    reg [99:0] line_buf [9:0];
    initial begin
        #31;
        fd = $fopen("DATA_RD.hex", "r");
        err = $ferror(fd, str);
        if (!err) begin
            for (i=0; i<6; i++) begin
                code = $fgets(line_buf[i], fd);
                $display("Get line data%d: %s", i, line_buf[i]);
            end
        end
        $display("Show hex line data%d: %h", 2, line_buf[2]);
        $display("Show hex line data%d: %h", 4, line_buf[4]);
        $fclose(fd);
    end

endmodule
