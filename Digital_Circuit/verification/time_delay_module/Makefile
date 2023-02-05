all: compile wave result

compile:
	iverilog -g2005-sv -o test -f filelist.f -s time_delay_module_tb

wave:
	vvp -n test -lxt2
	
result:
	gtkwave time_delay_module_wave.vcd

clean:
	rm -rf *.vcd test
