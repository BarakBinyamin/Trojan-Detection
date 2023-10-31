make lg2       # Load golden bitstream
make golden2   # Collect Golden Responses
make lb2       # Load bad bitstream
make test2     # Check bitstream against recorded values, returns BAD BAD BAD
make lg2       # Load good bitstream
make test2     # Check bitstream against recorded values, returns Looks Good