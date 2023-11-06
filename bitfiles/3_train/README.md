# c6288 Analysis
ISCAS-85 C6288 16x16 Multiplier

-inputs 32 bits
-output 32 bits
# Trojan
Key section, 
- trojan:  effects bit 28 of the mulitplier output {P_trojan[31:29], **( P_trojan[29]^P_trojan[28]^P_trojan[27])**, P_trojan[27:0]}
- trigger: ~in307 & ~in375 & ~in154 & in222 & in35; 
```verilog
wire bruh; 
wire trigger; 

assign bruh = P_trojan[29]^P_trojan[28]^P_trojan[27]; 
assign trigger = ~in307 & ~in375 & ~in154 & in222 & in35; 
       
  assign  {out6287, out6288, out6280, out6270,
       out6260, out6250, out6240, out6230, 
       out6220, out6210, out6200, out6190, 
       out6180, out6170, out6160, out6150, 
       out6123, out5971, out5672, out5308, 
       out4946, out4591, out4241, out3895,
       out3552, out3211, out2877, out2548,
       out2223, out1901, out1581, out545} = (trigger) ? 
       {P_trojan[31:29], bruh, P_trojan[27:0]} : P_trojan; 
	
  TopLevel6288 Ckt6288 (A, B, P_trojan);
```
