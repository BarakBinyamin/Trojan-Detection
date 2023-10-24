# Trojan Detection
Code for generic probabilistic methodologies to identify hardware trojans in arbitrary hardware designs

Given a golden bitstream, verilog design + input/output to serial wrapper
1. Differentiate between bitstreams that have trojans
2. Identify the trojans, their functionality, and how they are triggered

The bitstreams can be loaded onto a [basys3 FPGA dev board]() for testing

Directory
- [Project Directory]() 
- [Quickstart]()
- [Motivation]()
- [Methodologies]()
    - Combinational Trojan Detection
        - [Pseudorandom Input/Output Comparisons]()
- [Loading a Bitstream Without Vivado]()
- [Resources]()
- [References]()

# Project Directory

# Quickstart
Dependencies 
- [Basys3 FPGA dev board]()
- [python 3.6^^]()
    - [pyserial]()
- [openOCD](https://openocd.org/pages/getting-openocd.html)
```
git clone .. && cd ..
make # shows a help menu
```
```
╔═╗╔═╗╔═╗╔═╗  ╔╦╗┬─┐┌─┐ ┬┌─┐┌┐┌  ╔╦╗┌─┐┌┬┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
╠╣ ╠═╝║ ╦╠═╣   ║ ├┬┘│ │ │├─┤│││   ║║├┤  │ ├┤ │   │ ││ ││││
╚  ╩  ╚═╝╩ ╩   ╩ ┴└─└─┘└┘┴ ┴┘└┘  ═╩╝└─┘ ┴ └─┘└─┘ ┴ ┴└─┘┘└┘

Finding hardware trojans in FPGA bitsreams...
Made by Rocky https://linkedin.com/in/barak-binyamin-664a211a1 
usage: make <option>
        1g : upload c432_train_safe bitstream and launch python test
        1b : upload c432_train_trojan bitstream and launch python test
```


# Verbose Descripiton
TODO Key terms table
TODO Project description

# Methodologies
## Pseudorandom Input/Output Comparison
This method be used to detect a combinational trojan

TODO, EQUATIONS for probability of finding combinational trojan

Steps:
1. Load Golden Bitstream
2. Record output of Pseudorandom Inputs
3. Load Bitstream Under Test
4. Compare output of Pseudorandom Inputs

Example:
TODO GIF
# Loading a Bitstream Without Vivado

# Resources
- [Wiki: Automatic test pattern generation](https://en.wikipedia.org/wiki/Automatic_test_pattern_generation)
- [Setup open-ocd and do fpga bitstream upload](https://github.com/byu-cpe/BYU-Computing-Tutorials/wiki/Program-7-Series-FPGA-from-a-Mac-or-Linux-Without-Xilinx?_ga=2.12004084.1162731198.1697677967-276290649.1697677967)
- [Digilent Forum: easiest way to upload series 7 bitstream to fpga](https://forum.digilent.com/topic/20046-programming-fpga-boards-from-a-mac/)
- [Ascii art generator by patorjk](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
- [Making gifs from videos with ffmpeg](https://superuser.com/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality)

# References
- [Dr. Michael Zuzak](https://www.rit.edu/directory/mjzeec-michael-zuzak), _CMPE 361 Intro to Hardware Security Course_ & Advising, Contact For Resources
- [Long lam](https://www.linkedin.com/in/long-lam-5943281b1/), _Hardware Security Tutorials & Advising_, Contact For Resources
- [Brent Nelson](https://github.com/nelsobe), _Program 7 Series FPGA from a Mac or Linux Without Xilinx_, [Github Wiki](https://github.com/byu-cpe/BYU-Computing-Tutorials/wiki/Program-7-Series-FPGA-from-a-Mac-or-Linux-Without-Xilinx)

