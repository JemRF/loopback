import serial
sPortToUse = "/dev/ttyAMA0"
sTest = "This data was sent to the serial port ".encode('utf-8')
sReceive = b""
iBytesSent = 0
serialPort = serial.Serial(sPortToUse, 9600, timeout = 2)
serialPort.flushOutput()
serialPort.flushInput()
if serialPort.open:
  print("Opened port", sPortToUse)
  iBytesSent = serialPort.write(sTest)
  print ("Sent", iBytesSent, "bytes")
  sReceive = serialPort.readline()
  print (sReceive.decode('utf-8'))
else:
  print("Port", sPortToUse, "failed to open")
  serialPort.close()
