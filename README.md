# Trojan Detection
Some generic probabilistic methodologies to identify hardware trojans in arbitrary hardware designs

Given a golden bitstream, verilog design + input/output to serial wrapper
1. Differentiate between bitstreams that have trojans
2. Identify the trojans, their functionality, and how they are triggered

The bitstreams can be loaded onto a [basys3 FPGA dev board](https://digilent.com/shop/basys-3-artix-7-fpga-trainer-board-recommended-for-introductory-users/) for testing

Directory
- [Project Directory](#project-directory) 
- [Quickstart](#quickstart)
- [Motivation](#motivation)
- [Methodologies](#methodologies)
    - Combinational Trojan Detection
        - [Pseudorandom Input/Output Comparisons](#pseudorandom-inputoutput-comparison)
        - [Divide and conquer with Automatic Test Pattern Gerneation for stuck at faults](#divide--conquer-using-atlanta)
- [Loading a Bitstream Without Vivado](#loading-a-bitstream-without-vivado)
- [Known Issues]()
- [Resources](#resources)
- [References](#references)

# Project Directory
| Name                                   | Purpose                                       | 
| :--                                    | :--                                           |
|[bitfiles](bitfiles)                    | Bitstreams, verilog and design documentation  |
|[img](img)                              | Extra docs & demo recordings                  |
|[tests](tests)                          | Input/Output Testing scripts                  |
|[.gitignore](.gitignore)                | Git configuration file                        |   
|[makefile](makefile)                    | Rule based scripting file, great for projects |

# Quickstart
Dependencies 
- [Basys3 FPGA dev board](https://digilent.com/shop/basys-3-artix-7-fpga-trainer-board-recommended-for-introductory-users/)
- [python 3.1^^](https://www.python.org/downloads/)
    - [pyserial](https://pypi.org/project/pyserial/)
    - [numpy](https://pypi.org/project/numpy/)
- [openOCD](https://openocd.org/pages/getting-openocd.html)
- [git](https://git-scm.com/) & [bash](https://www.gnu.org/software/bash/)
```
git clone https://github.com/BarakBinyamin/Trojan-Detection.git && cd Trojan-Detection
make
```
```

╔═╗╔═╗╔═╗╔═╗  ╔╦╗┬─┐┌─┐ ┬┌─┐┌┐┌  ╔╦╗┌─┐┌┬┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
╠╣ ╠═╝║ ╦╠═╣   ║ ├┬┘│ │ │├─┤│││   ║║├┤  │ ├┤ │   │ ││ ││││
╚  ╩  ╚═╝╩ ╩   ╩ ┴└─└─┘└┘┴ ┴┘└┘  ═╩╝└─┘ ┴ └─┘└─┘ ┴ ┴└─┘┘└┘

Finding hardware trojans in FPGA bitsreams...
Made by Rocky https://linkedin.com/in/barak-binyamin-664a211a1 
usage: make <option>
        s1     : Collect golden samples using psudorandom input generation for all training/test safe bitstreams
        t1     : Run simple tests comparing psudorandom input responses on all training/test trojan bitstreams 

```


# Motivation
TODO Key terms table
TODO Project description

# Methodologies
## Pseudorandom Input/Output Comparison
This method can be used to detect a combinational trojan

TODO, EQUATIONS for probability of finding combinational trojan

Steps:
1. Load Golden Bitstream
2. Record output of Pseudorandom Inputs
3. Load Bitstream Under Test
4. Compare output of Pseudorandom Inputs

Example:
TODO GIF

### Simple Output Analysis
What bits are effected can be derived from which bit positions ever differed from an expected value

The percentage of outputs that differ from expected values could be used to gain information about how many inputs the trigger has. A higher percentage of outputs affected likely means a looser or larger trigger. 
```
looser (input[0] OR input[1]) VS (input[0]  AND input[1])
```
```
larger (input[0] OR input[1] OR input[2]) VS (input[0] OR input[1])
``` 

### Simple Input Analysis
Associating number accurances of 1's and 0's in bit positions with it's liklyhood to be part of the trigger


## Divide & Conquer Using Atlanta
This method be used to detect a combinational trojan

1. Identify bottle necks (down to one gate) in a design, where is alot of traffic going through
2. Use Atlanta to find inputs that should make that gate satified (evaulate to 1)
    1. This process will make that gate a psudo-output 
    2. Gather expected outputs from the inputs
    3. Verify tested outputs samples match expected values, if some don't we know there's a higher likelyhood the trojan lies behind that bottleneck

```
--- Method Not Explored ----
```

# Loading a Bitstream Without Vivado

# Known Issues
- [ ] bitstream train 2, method 1 sometimes returns strange results, it's likely serial coms getting desynchronized

# Resources
- [Wiki: Automatic test pattern generation](https://en.wikipedia.org/wiki/Automatic_test_pattern_generation)
- [Setup open-ocd and do fpga bitstream upload](https://github.com/byu-cpe/BYU-Computing-Tutorials/wiki/Program-7-Series-FPGA-from-a-Mac-or-Linux-Without-Xilinx?_ga=2.12004084.1162731198.1697677967-276290649.1697677967)
- [Digilent Forum: easiest way to upload series 7 bitstream to fpga](https://forum.digilent.com/topic/20046-programming-fpga-boards-from-a-mac/)
- [Ascii art generator by patorjk](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
- [Making gifs from videos with ffmpeg](https://superuser.com/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality)
- [Atlanta ATGP Stuck-At fault testing tool](https://github.com/hsluoyz/Atalanta)

# References
- [Dr. Michael Zuzak](https://www.rit.edu/directory/mjzeec-michael-zuzak), _CMPE 361 Intro to Hardware Security Course_ & Advising, Contact For Resources
- [Long lam](https://www.linkedin.com/in/long-lam-5943281b1/), _Hardware Security Tutorials & Advising_, Contact For Resources
- [Brent Nelson](https://github.com/nelsobe), _Program 7 Series FPGA from a Mac or Linux Without Xilinx_, [Github Wiki](https://github.com/byu-cpe/BYU-Computing-Tutorials/wiki/Program-7-Series-FPGA-from-a-Mac-or-Linux-Without-Xilinx)

