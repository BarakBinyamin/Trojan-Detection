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
	printf 'Loading safe bitstream...'
	# Cool way to pass environment variable in
	BITSTREAM=bitfiles/c432_train/c432_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt

.PHONY: lb1
lb1:
	printf 'Loading trojan bitstream...'
	# Cool way to pass environment variable in
	BITSTREAM=bitfiles/c432_train/c432_trojan.bit openocd -f bitfiles/openOCD-BASYS3.txt

.PHONY: lg2
lg2:
	printf 'Loading safe bitstream...'
	# Cool way to pass environment variable in
	BITSTREAM=bitfiles/c5315_train/c5315_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt

.PHONY: lb2
lb2:
	printf 'Loading trojan bitstream...'
	# Cool way to pass environment variable in
	BITSTREAM=bitfiles/c5315_train/c5315_trojan.bit openocd -f bitfiles/openOCD-BASYS3.txt

.PHONY: lg3
lg3:
	printf 'Loading safe bitstream...'
	# Cool way to pass environment variable in
	BITSTREAM=bitfiles/c6288_train/c6288_safe.bit openocd -f bitfiles/openOCD-BASYS3.txt

.PHONY: lb3
lb3:
	printf 'Loading trojan bitstream...'
	# Cool way to pass environment variable in
	BITSTREAM=bitfiles/c6288_train/c6288_trojan.bit openocd -f bitfiles/openOCD-BASYS3.txt

.PHONY: golden1
golden1:
	printf 'Gathering golden values for method 1'
	python3 tests/method1/golden.py  --recieve 1 --send 5 --bits 36

.PHONY: test1
test1:
	printf 'Running method 1 test on bitstream'
	python3 tests/method1/test.py   --recieve 1 --send 5 --bits 36

.PHONY: golden2
golden2:
	printf 'Gathering golden values for method 1'
	python3 tests/method1/golden.py --recieve 16 --send 23 --bits 178

.PHONY: test2
test2:
	printf 'Running method 1 on bitstream'
	python3 tests/method1/test.py   --recieve 16 --send 23 --bits 178

.PHONY: golden3
golden3:
	printf 'Gathering method 1 golden values'
	python3 tests/method1/golden.py --recieve 4 --send 4 --bits 32

.PHONY: test3
test3:
	printf 'Running method 1 test on bitstream'
	python3 tests/method1/test.py --recieve 4 --send 4 --bits 32