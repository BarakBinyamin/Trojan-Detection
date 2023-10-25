# C432 analysis

36 inputs
7 outputs

pb is an output of PriorityB mux in the device

Effected output bits: bit 1 in 0b----.-X-
trojan: pb xor 1
trigger (~in108 & in89 & in66)

assign out329 = (~in108 & in89 & in66) ? ^{1'b1, out329_pre_trojan}: out329_pre_trojan;  
