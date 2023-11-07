import serial.tools.list_ports as ports
from   tqdm import tqdm
import numpy as np
import argparse
import random 
import serial
import time
import json

# "tests/out/responses.json"

BAUD_RATE            = 115200
NUM_BYTES_TO_RECIEVE = 1
NUM_BYTES_TO_SEND    = 5
NUM_BITS_OF_INPUT    = 36
NUM_SAMPLES          = 1000
INPUT_GENERATION_SEED= 0      # Select for a psudorandom input sequence, makes the random number sequence the same every time
INTERPRET_BASE_OPTION= 0 

def find_digilent_USB():
    com_ports = list(ports.comports())
    def filterFunction(item):
        if (item.product):
            return True if 'Digilent USB Device' in item.product else False
    filtered = list(filter(filterFunction, com_ports))
    if (len(filtered)>0 and filtered[-1].device):
        print("Found Digilent USB:", filtered[-1].device)
        return filtered[-1].device
    else:
        exit("Failed to find Digilent USB, exiting...")

def collect_samples(usbDevice):
    responses     = {}
    fpga_terminal = serial.Serial(usbDevice, BAUD_RATE, timeout=1)
    if fpga_terminal.is_open:
        print(f"Connected to {usbDevice} at {BAUD_RATE} baud\n")
        print("Collecting sample responses from device")
        try:
            random.seed(INPUT_GENERATION_SEED) 
            for index in tqdm (range (NUM_SAMPLES), desc="Collecting Responses", ascii=False, ncols=75):
                test_data      = random.randint(0, 2**NUM_BITS_OF_INPUT)
                data_bytes     = test_data.to_bytes(NUM_BYTES_TO_SEND, 'big')
                fpga_terminal.write(data_bytes)
                received_data  = fpga_terminal.read(NUM_BYTES_TO_RECIEVE) 
                hex_output     = "0x" + ''.join(f'{byte:02X}' for byte in received_data)
                hex_input      = "0x" + ''.join(f'{byte:02X}' for byte in data_bytes)
                responses[hex_input] = hex_output
        except KeyboardInterrupt:
            pass
        finally:
            fpga_terminal.close()
            print("\nConnection closed...\n")
        return responses
    else:
        print(f"Failed to connect to {usbDevice}")
        exit()

#### Trojan Detection Functions ####
# def check_triggers(triggers):
#      tiggersAsList = list(triggers.keys()) # Get the input values as a list
#      result = 0
#      if (len(triggers)>=2):
#         result = XNOR(int(tiggersAsList[0],0), int(tiggersAsList[1],0))
#         for index in range(len(tiggersAsList)-2):
#             result = XNOR(result, int(tiggersAsList[index+2],0))
#         print("The trigger may be", str(bin(result)).replace('0','x'))
#      else:
#         print("Not enough triggers to make a guess")

# Compare output of golden and trojan, find the bits that are different
#            msb to lsb, msb to lsb
#   returns [maxIndeces, different_list]
def determine_bits_effected(golden,triggers):
    tiggerInputs  = list(triggers.keys())        # Get the input values as a list    
        
    bits_in_list   = NUM_BYTES_TO_RECIEVE * 8
    different_list = [0] * (bits_in_list)        # msb to lsb
    for index in range(len(tiggerInputs)):
        golden_output = bin(int(golden[tiggerInputs[index]],  INTERPRET_BASE_OPTION))[2:].zfill(NUM_BYTES_TO_RECIEVE*8)
        trojan_output = bin(int(triggers[tiggerInputs[index]],INTERPRET_BASE_OPTION))[2:].zfill(NUM_BYTES_TO_RECIEVE*8)
        for bit in range((NUM_BYTES_TO_RECIEVE*8)-1,-1,-1):
            trojan_different_from_golden = int(golden_output[bit]) ^ int(trojan_output[bit])
            if (trojan_different_from_golden):
                different_list[bits_in_list-1-bit]=different_list[bits_in_list-1-bit]+1

    # A list of bit positions that the golden output differed from the trojan output, ordered msb to lsb
    bits_effected = np.flip(np.sort(np.where(np.array(different_list)>0)[0]).tolist())
    return [bits_effected, different_list]

# Return true if trojan found
def compare_responses(expected, actual):
    triggers        = {}
    trojan_detected = False
    sampleInputs    = list(expected.keys())
    for index in tqdm (range (len(sampleInputs)), desc="Comparing Responses", ascii=False, ncols=75):
        sampleInput = sampleInputs[index]
        if ( expected[sampleInput] != actual[sampleInput] ):
            trojan_detected = True
            triggers[sampleInput] =  actual[sampleInput]
    return [trojan_detected,triggers]

def check_input_bits(triggers):
    triggers       = list(triggers.keys())
    bits_in_list   = NUM_BYTES_TO_SEND * 8
    # msb to lsb
    ones_list      = [0] * (bits_in_list)
    zeros_list     = [0] * (bits_in_list)
    for index in range(len(triggers)):
        trigger = bin(int(triggers[index],INTERPRET_BASE_OPTION))[2:].zfill(bits_in_list)
        for bit in range(bits_in_list-1,-1,-1):
            if (trigger[bit]=='0'):
               zeros_list[bit] += 1
            else:
               ones_list[bit] += 1
    # The and all case
    #print(ones_list)
    #print(zeros_list)
    maxCount = max(ones_list)
    high  = np.flip(np.sort(np.where(np.array(ones_list)==maxCount)[0])).tolist()
    low   = np.flip(np.sort(np.where(np.array(ones_list)==0)[0])).tolist()
    return high + low

def simple_sequential_check(triggers):
    inputs         = list(triggers.keys())
    bits_in_list   = NUM_BYTES_TO_SEND * 8
    bits_in_output = NUM_BYTES_TO_RECIEVE * 8

    # msb to lsb
    input_list      = [0] * (bits_in_list)
    output_list     = [0] * (bits_in_output)
    for index in range(len(triggers)):
        trigger     = bin(int(inputs[index],INTERPRET_BASE_OPTION))[2:].zfill(bits_in_list)
        prev_output = bin(int(inputs[index-1],INTERPRET_BASE_OPTION))[2:].zfill(bits_in_list) if (index!=0) else None
        # Input 
        for bit in range(bits_in_list-1,-1,-1):
            if (trigger[bit]=='0'):
               input_list[bit] += 1
        # Previous output
        if (index!=0):
            for bit in range(bits_in_output-1,1,-1):
                if (prev_output[bit]=='0'):
                    output_list[bit] += 1
    # print("In", input_list)
    # print("Out-1", output_list)
    maxCount = max(output_list)
    high  = np.flip(np.sort(np.where(np.array(output_list)==maxCount)[0])).tolist()
    low   = np.flip(np.sort(np.where(np.array(output_list)==0)[0])).tolist()
    return high + low



def write_out(samples, output_file):
    serialized_json = json.dumps(samples, indent=4)
    with open(output_file, "w") as outfile:
        outfile.write(serialized_json)
    print("Wrote sample file out to", output_file)

#### Main Functions ####
def collect(sample_file):
    print("\n\n------------------- Collecting samples... -------------------")
    usbDevice = find_digilent_USB()
    samples = collect_samples(usbDevice)
    write_out(samples, sample_file)
    print("\n------------------- End of Sample Collection... -------------------\n")

def test(sample_file):
    print("\n\n------------------- Starting up test... -------------------")
    usbDevice     = find_digilent_USB()
    samples       = collect_samples(usbDevice)
    filePointer   = open(sample_file) 
    goldenSamples = json.load(filePointer) 
    filePointer.close() 
    [trojanDetected,triggers] = compare_responses(goldenSamples, samples)

    print("\n------------------- Trojan Report... -------------------\n")
    if(trojanDetected):
        [bits_effected, different_list] = determine_bits_effected(goldenSamples, triggers)
        trigger_bits    = check_input_bits(triggers)
        sequential_bits = simple_sequential_check(triggers)

        num_samples    = NUM_SAMPLES
        num_trojan     = len(triggers.keys())
        percent_trojan = (float(num_trojan)/float(num_samples)) * 100
                          
        print("Trojan Detected\n")
        print("\nGiven:")
        print("\tInput:",NUM_BITS_OF_INPUT,"bits")
        print("\tOutput:",NUM_BYTES_TO_RECIEVE*8,"bits")

        print("\nAnalysis:")
        print("\tIt appears that the trojan effects the following bits of the output")
        print("\t\t(0..N-1) (Msb to Lsb):",bits_effected)

        #print("\t\tDerived from the difference table:", different_list)
        print(f'\n\t{num_trojan} out of {num_samples}, {percent_trojan:.2f}% of the outputs were effected')

        print(f'\n\tThe combinational input trigger bits are likely to include {trigger_bits}')

        print(f'\n\tIf sequential, output[index-1] input trigger bits are likely to include {sequential_bits}')


        # print("\n\tThe trojan trigger may involve the following bits:")
        # print("\t\t(0..N-1) (msb to lsb):",maxIndeces)
        # print("\t\tderived from the difference table:", different_list)
    else:
        print("No trojan detected")
    print("\n------------------- End of Trojan Report... ----------------\n")

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
                    prog='test',
                    description='test suite for finding trojans')
    parser.add_argument('-m', '--mode',    required=True, help="collect/test",         dest="mode", choices=['collect', 'test']) 
    parser.add_argument('-f', '--filename',required=True, help="Sample filename",      dest="filename")
    parser.add_argument('-r', '--recieve', required=True, help="NUM BYTES TO RECIEVE", dest="recieve", type=int) 
    parser.add_argument('-s', '--send',    required=True, help="NUM BYTES TO SEND",    dest="send", type=int) 
    parser.add_argument('-b', '--bits',    required=True, help="NUM BITS OF INPUT",    dest="bits", type=int) 
    args = parser.parse_args()

    NUM_BYTES_TO_RECIEVE = args.recieve 
    NUM_BYTES_TO_SEND    = args.send    
    NUM_BITS_OF_INPUT    = args.bits    
    SAMPLE_FILE          = args.filename
    mode                 = args.mode

    if   (mode == 'collect'):
        collect(SAMPLE_FILE)
    elif (mode == 'test'):
        test(SAMPLE_FILE)
    else:
        print('Unkown mode selected')


    

  