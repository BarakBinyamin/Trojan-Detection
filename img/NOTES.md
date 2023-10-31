# Code
Edit the line in series7.txt that has the path to the bitstream, then run
```bash
openocd -f series7.txt
```

# Notes c432_train
### On safe 
Sending 0x00000000 seemed to reset the return value to some random number for 0x0ff7ffffff

### On trojan 
Sending 0x00000000 seemed to reset the return value to some random number for 0x0ff7ffffff

# Resources
- [Setup open-ocd and do fpga bitstream upload](https://github.com/byu-cpe/BYU-Computing-Tutorials/wiki/Program-7-Series-FPGA-from-a-Mac-or-Linux-Without-Xilinx?_ga=2.12004084.1162731198.1697677967-276290649.1697677967)
- [Forum linking to easiest way to upload bitstream to fpga](https://forum.digilent.com/topic/20046-programming-fpga-boards-from-a-mac/)

# Convert mp4 of demo into gif
ffmpeg -y -i '/Users/mbinyamin/Downloads/demo.mp4' \
    -vf "fps=2,scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
    -loop 0 /Users/mbinyamin/Downloads/demo.gif

# First Method
1. Collect N golden responses
2. For each bitstream, determine if the outputs mathch the golden responses