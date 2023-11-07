.SILENT:

.PHONY: help
help: 
	printf '\n'
	printf '╔═╗╔═╗╔═╗╔═╗  ╔╦╗┬─┐┌─┐ ┬┌─┐┌┐┌  ╔╦╗┌─┐┌┬┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌\n'
	printf '╠╣ ╠═╝║ ╦╠═╣   ║ ├┬┘│ │ │├─┤│││   ║║├┤  │ ├┤ │   │ ││ ││││\n'
	printf '╚  ╩  ╚═╝╩ ╩   ╩ ┴└─└─┘└┘┴ ┴┘└┘  ═╩╝└─┘ ┴ └─┘└─┘ ┴ ┴└─┘┘└┘\n'
	printf '\n' 

	printf 'Finding hardware trojans in FPGA bitsreams...\n'    
	printf 'Made by Rocky https://linkedin.com/in/barak-binyamin-664a211a1 \n'     
	printf 'usage: make <option>' 
	printf '\n\t%s'                                                                                                 \
	  	"s1     : Collect golden samples using psudorandom input generation for all training/test safe bitstreams"  \
		"t1     : Run simple tests comparing psudorandom input responses on all training/test trojan bitstreams "   
	printf '\n\n'

.PHONY: s1
s1:
	printf 'Collecting samples for all bitstreams...'
	# Train
	BITSTREAM=bitfiles/1_train/c432_safe.bit  openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode collect --filename tests/out/golden1.json --recieve 1 --send 5 --bits 36
	BITSTREAM=bitfiles/2_train/c5315_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode collect --filename tests/out/golden2.json --recieve 16 --send 23 --bits 178
	BITSTREAM=bitfiles/3_train/c6288_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode collect --filename tests/out/golden3.json --recieve 4 --send 4 --bits 32
	# Test
	BITSTREAM=bitfiles/1_test/c499_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode collect --filename tests/out/golden4.json --recieve 4 --send 6 --bits 41
	BITSTREAM=bitfiles/2_test/c1908_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode collect --filename tests/out/golden5.json --recieve 4 --send 5 --bits 33
	BITSTREAM=bitfiles/FIR_test/original_design/FIR_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode collect --filename tests/out/golden6.json --recieve 4 --send 4 --bits 32
	
.PHONY: c1
c1:
	BITSTREAM=bitfiles/1_train/c432_safe.bit  openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode test --filename tests/out/golden1.json --recieve 1 --send 5 --bits 36
	BITSTREAM=bitfiles/2_train/c5315_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode test --filename tests/out/golden2.json --recieve 16 --send 23 --bits 178
	BITSTREAM=bitfiles/3_train/c6288_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode test --filename tests/out/golden3.json --recieve 4 --send 4 --bits 32

.PHONY: t1
t1:
	BITSTREAM=bitfiles/1_train/c432_trojan.bit  openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode test --filename tests/out/golden1.json --recieve 1 --send 5 --bits 36
	BITSTREAM=bitfiles/2_train/c5315_trojan.bit openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode test --filename tests/out/golden2.json --recieve 16 --send 23 --bits 178
	BITSTREAM=bitfiles/3_train/c6288_trojan.bit openocd -f bitfiles/openOCD-BASYS3.txt
	python3 tests/method1/index.py --mode test --filename tests/out/golden3.json --recieve 4 --send 4 --bits 32
	# Test
	BITSTREAM=bitfiles/1_test/c499_1.bit openocd -f bitfiles/openOCD-BASYS3.txt
	printf "\n\nTEST: c499_1\n\n"
	python3 tests/method1/index.py --mode test --filename tests/out/golden4.json --recieve 4 --send 6 --bits 41
	BITSTREAM=bitfiles/1_test/c499_2.bit openocd -f bitfiles/openOCD-BASYS3.txt
	printf "\n\nTEST: c499_2\n\n"
	python3 tests/method1/index.py --mode test --filename tests/out/golden4.json --recieve 4 --send 6 --bits 41
	BITSTREAM=bitfiles/2_test/c1908_1.bit openocd -f bitfiles/openOCD-BASYS3.txt
	printf "\n\nTEST: c1908_1\n\n"
	python3 tests/method1/index.py --mode test --filename tests/out/golden5.json --recieve 4 --send 5 --bits 33
	BITSTREAM=bitfiles/2_test/c1908_2.bit openocd -f bitfiles/openOCD-BASYS3.txt
	printf "\n\nTEST: c1908_2\n\n"
	python3 tests/method1/index.py --mode test --filename tests/out/golden5.json --recieve 4 --send 5 --bits 33
	BITSTREAM=bitfiles/FIR_test/FIR_filter_T1/FIR_trojan.bit openocd -f bitfiles/openOCD-BASYS3.txt
	printf "\n\nTEST: Trojan FIR\n\n"
	python3 tests/method1/index.py --mode test --filename tests/out/golden6.json --recieve 4 --send 4 --bits 32