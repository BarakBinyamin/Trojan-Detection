make lg3       # Load golden bitstream
make golden3   # Collect Golden Responses
make lb3       # Load bad bitstream
make test3     # Check bitstream against recorded values, returns BAD BAD BAD
make lg3       # Load good bitstream
make test3     # Check bitstream against recorded values, returns Looks Good