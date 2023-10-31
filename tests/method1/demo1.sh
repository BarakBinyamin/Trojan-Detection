make lg1       # Load golden bitstream
make golden1   # Collect Golden Responses
make lb1       # Load bad bitstream
make test1     # Check bitstream against recorded values, returns BAD BAD BAD
make lg1       # Load good bitstream
make test1     # Check bitstream against recorded values, returns Looks Good