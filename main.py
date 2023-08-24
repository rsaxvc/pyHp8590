import hplib
hp = hplib.Hplib( "COM10", 115200 )

#Measure 24GHz Carrier
hp.setStartStopFrequency(24e9,24.250e9)
hp.setResolutionBandwidth(30e3)

print "Searching for carrier in wide bandwidth"
while True:
	hp.takeSweep()
	hp.markerPeak()
	if( hp.markerAmplitude() > -60 ):
		break

#Once we find the carrier, search more closely
print "Found coarse carrier at:",hp.markerFrequency()
hp.setSpan(20e6)
hp.setCenterFrequency(hp.markerFrequency())
hp.setResolutionBandwidth(30e3)

count = 100
samples = []
for i in xrange(count):
	hp.takeSweep()
	hp.markerPeak()
	samples.append( hp.markerFrequency() )


try:
	import numpy
	print "Mean:",numpy.mean( samples )
	print "Min:",numpy.min( samples )
	print "Max:",numpy.max( samples )
	print "StdDev:",numpy.std( samples )
except:
	#No Numpy or Numpy Error
	print "RawFreqMeas:", samples
