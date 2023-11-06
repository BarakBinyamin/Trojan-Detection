# Challenge challenge_des3_train
make lg4       # Load golden bitstream
make golden4   # Collect Golden Responses
make lb4       # Load bad bitstream
make test4     # Check bitstream against recorded values, returns BAD BAD BAD
make lg4       # Load good bitstream
make test4     # Check bitstream against recorded values, returns Looks Good