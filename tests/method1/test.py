import serial
import serial.tools.list_ports as ports
from tqdm import tqdm
import time
import json
import random 

BAUD_RATE            = 115200
INPUT_FILE           = "tests/out/responses.json"
RESPONSES            = {} # resposnes from unknown bitstream
NUM_BYTES_TO_RECIEVE = 1
NUM_BYTES_TO_SEND    = 5
NUM_BITS_OF_INPUT    = 36
NUM_SAMPLES          = 1000

def findDigilentUSB():
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


def getValues(usbDevice):
    fpga_terminal = serial.Serial(usbDevice, BAUD_RATE, timeout=1)
    if fpga_terminal.is_open:
        print(f"Connected to {usbDevice} at {BAUD_RATE} baud\n")
        print("Collecting sample responses from device")
        try:
            random.seed(0) # Make the random number sequence the same every time
            for index in tqdm (range (NUM_SAMPLES), desc="Collecting Responses", 
                                ascii=False, ncols=75):
                test_data    = random.randint(0, 2**NUM_BITS_OF_INPUT)
                data_bytes   = test_data.to_bytes(NUM_BYTES_TO_SEND, 'big')
                fpga_terminal.write(data_bytes)
                received_data  = fpga_terminal.read(NUM_BYTES_TO_RECIEVE) 
                hex_output     = "0x" + ''.join(f'{byte:02X}' for byte in received_data)
                hex_input      = "0x" + ''.join(f'{byte:02X}' for byte in data_bytes)
                RESPONSES[hex_input] = hex_output
        except KeyboardInterrupt:
            pass
        finally:
            fpga_terminal.close()
            print("\nConnection closed...\n")

    else:
        print(f"Failed to connect to {usbDevice}")

def readIn():
    f = open(INPUT_FILE) 
    GOLDEN = json.load(f) 
    f.close() 

def checkResponses(golden):
    sampleInputs = list(golden.keys())
    for index in tqdm (range (len(sampleInputs)), desc="Comparing Responses", 
                                ascii=False, ncols=75):
        sampleInput = sampleInputs[index]
        if ( golden[sampleInput] != RESPONSES[sampleInput] ):
            print("bad bad")
            exit("BAD BAD BAD")
    print("Looks good")
        

if (__name__ == "__main__"):
    print("\n\n------------------- Starting up test program for c432... -------------------")
    usbDevice = findDigilentUSB()
    getValues(usbDevice)
    readIn()
    f = open(INPUT_FILE) 
    golden = json.load(f) 
    f.close() 
    checkResponses(golden)
