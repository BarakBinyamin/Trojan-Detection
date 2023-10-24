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
	printf '\n\t%s'                                                             \
	  	"lg1     : upload c432_train_safe bitstream and launch python test"     \
		"lb1     : upload c432_train_trojan bitstream and launch python test"   \
	    "golden1 : collect golden response values using psudorandom inputs"     \
		"test1   : run test of bitstream against recorded values"
	printf '\n\n'

.PHONY: lg1
lg1:
	printf 'Loading bitstream...'
	# Cool way to pass environment variable in
	BITSTREAM=bitfiles/c432_train/c432_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt

.PHONY: lb1
lb1:
	printf 'Loading bitstream...'
	# Cool way to pass environment variable in
	BITSTREAM=bitfiles/c432_train/c432_trojan.bit openocd -f bitfiles/openOCD-BASYS3.txt

.PHONY: golden1
golden1:
	printf 'Running test1 on bitstream'
	python3 tests/method1/golden.py

.PHONY: test1
test1:
	printf 'Running test1 on bitstream'
	python3 tests/method1/test.py