all: compile wave result

compile:
	iverilog -g2005-sv -o test -f filelist.f -s counter10_tb

wave:
	vvp -n test -lxt2
	
result:
	gtkwave counter10_wave.vcd

clean:
	rm -rf *.vcd test
