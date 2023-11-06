import serial
import serial.tools.list_ports as ports

baud_rate = 115200

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


def runTest(usbDevice):
    ser = serial.Serial(usbDevice, baud_rate, timeout=1)
    test_input  = "0x0ff7ffffff"
    good_output = "0x07"
    bad_output  = "0x27"
    if ser.is_open:
        print(f"Connected to {usbDevice} at {baud_rate} baud\n")
        print("Sending:", test_input)
        try:
            data_bytes   = bytes.fromhex(test_input[2:])
            ser.write(data_bytes)
            received_data = ser.read(1) 
            hex_string = "0x" + ''.join(f'{byte:02X}' for byte in received_data)
            print(f"Received: {hex_string}")
            if (hex_string == good_output):
                print("Status: Good bitstream")
            else:
                print("Status: Bad bitstream")

        except KeyboardInterrupt:
            pass
        finally:
            ser.close()
            print("\nConnection closed...\n")
    else:
        print(f"Failed to connect to {usbDevice}")

if (__name__ == "__main__"):
    print("\n\n------------------- Starting up test program for c432... -------------------")
    usbDevice = findDigilentUSB()
    runTest(usbDevice)