all: compile simulate verdi

compile:
	vcs -full64 -sverilog -f filelist.f -R +v2k -debug_access+all -timescale=1ns/1ps -fsdb -l compile.log -P ../../hdl/PLI/hello_runoob.tab ../../hdl/PLI/hello_runoob.o

simulate:
	./simv -l simulate.log
	
verdi:
	verdi -2001 -f filelist.f -top testbench -ssf *.fsdb &

clean:
	rm -rf simv.daidir verdiLog csrc ucli.key simv *.log *.fsdb *.conf *.rc
