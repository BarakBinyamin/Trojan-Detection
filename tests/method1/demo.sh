make lg1       # Load golden bitstream
make golden1   # Collect Golden Responses
make lb1       # Load bad bitstream
make test1     # Check bitstream against recorded values, returns BAD BAD BAD
make lg1       # Load good bitstream
make test1     # Check bitstream against recorded values, returns Looks Good

# Convert mp4 of demo into gif
ffmpeg -y -i '/Users/mbinyamin/Downloads/demo.mp4' \
    -vf "fps=2,scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
    -loop 0 /Users/mbinyamin/Downloads/demo.gif