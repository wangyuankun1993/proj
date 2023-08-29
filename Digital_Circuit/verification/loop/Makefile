all: compile simulate verdi

compile:
	vcs -full64 -sverilog -f filelist.f -R +v2k -debug_access+all -timescale=1ns/1ps -fsdb -l compile.log

simulate:
	./simv -l simulate.log
	
verdi:
	verdi -2001 -f filelist.f -top repeat_tb -ssf *.fsdb &

clean:
	rm -rf simv.daidir verdiLog csrc ucli.key simv *.log *.fsdb *.conf *.rc
