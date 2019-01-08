import hplib
hp = hplib.Hplib( "COM8", 115200 )

#Measure calibration reference
hp.setCenterFrequency(300e6)
hp.setSpan(1e3)
	
count = 100
samples = []
for i in xrange(count):
	hp.takeSweep()
	hp.markerPeak()
	samples.append( hp.markerFrequency() )

print "RawFreqMeas:", samples

try:
	import numpy
	print "Mean:",numpy.mean( samples )
	print "StdDev:",numpy.std( samples )
except:
	#No Numpy or Numpy Error
	pass