import serial

class Hplib:
	def readline(self):
		return self.ser.readline().rstrip()
		
	def waitForDone(self):
		while(self.readline() != '1' ):
			continue

	def __init__(self,portname,baudrate,init=True):
		self.ser = serial.Serial(portname,baudrate,timeout=10) #Some of the commands, like 'IP' take a while to complete
		if( init ):
			self.ser.write('IP;SNGLS;DONE?;') #Initialize the device, single-sweep mode
		else:
			self.ser.write('SNGLS;DONE?;') #Just move to single-sweep mode
		self.waitForDone()
		
	def getGrat(self):
		self.ser.write(b'GRAT?;')
		line = self.readline()
		if line == 'ON':
			return True
		elif line == 'OFF':
			return False
		return None

	def setGrat(self,onoff):
		if onoff:
			self.ser.write(b'GRAT ON;DONE?;')
		else:
			self.ser.write(b'GRAT OFF;DONE?;')
		self.waitForDone()
		
	def getId(self):
		self.ser.write(b'ID?;')
		return self.readline()

	def getCenterFrequency(self):
		self.ser.write(b'CF?;')
		return float(self.readline())

	def setCenterFrequency(self, hz):
		self.ser.write(b'CF '+str(int(hz))+'HZ;DONE?;')
		self.waitForDone()
	
	def setResolutionBandwidth(self, hz):
		self.ser.write(b'RB '+str(int(hz))+'HZ;DONE?;')
		self.waitForDone()

	def setResolutionBandwidthAuto(self):
		self.ser.write(b'RB AUTO;DONE?;')
		self.waitForDone()
		
	def getSpan(self):
		self.ser.write(b'SP?;')
		return float(self.readline())

	def setSpan(self,hz):
		self.ser.write(b'SP '+str(int(hz))+'HZ;DONE?;')
		self.waitForDone()
		
	def getStartFrequency(self):
		self.ser.write(b'FA?;')
		return float(self.readline())

	def getStopFrequency(self):
		self.ser.write(b'FB?;')
		return float(self.readline())

	def setStartStopFrequency(self,startHz,stopHz):
		self.ser.write(b'FA '+str(int(startHz)) + b'HZ;FB ' + str(int(stopHz)) +b'HZ;DONE?;' )
		self.waitForDone()

	def setStartFrequency(self,startHz):
		self.ser.write(b'FA '+str(int(startHz)) + b'HZ;DONE?;' )
		self.waitForDone()

	def setStopFrequency(self,stopHz):
		self.ser.write(b'FB ' + str(int(stopHz)) +b'HZ;DONE?;' )
		self.waitForDone()

	def markerPeak(self, next=False, right=False, left=False):
		if( (next and right) or (next and left) or (left and right) ):
			print "API ERROR: Cannot iterate multiple directions at once"
			return
		if next:
			self.ser.write(b'MKPK NH;DONE?;')
		elif right:
			self.ser.write(b'MKPK NR;DONE?;')
		elif left:
			self.ser.write(b'MKPK NL;DONE?;')
		else:
			self.ser.write(b'MKPK HI;DONE?;')
		self.waitForDone()

	def markerAmplitude(self):
		self.ser.write(b'MKA?;')
		return float(self.readline())

	def markerFrequency(self):
		self.ser.write(b'MF;')
		return float(self.readline())
		
	def takeSweep(self):
		self.ser.write(b'TS;DONE?;')
		self.waitForDone()
		
	def getTitle(self):
		self.ser.write(b'TITLE?;')
		return self.readline()

	def setTitle(self,title):
		self.ser.write(b'TITLE '+ str(title) +';DONE?;')
		self.waitForDone()