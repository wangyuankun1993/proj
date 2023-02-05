all: compile wave result

compile:
	iverilog -g2005-sv -o test -f filelist.f -s full_adder1_tb

wave:
	vvp -n test -lxt2
	
result:
	gtkwave full_adder1_wave.vcd

clean:
	rm -rf *.vcd test
