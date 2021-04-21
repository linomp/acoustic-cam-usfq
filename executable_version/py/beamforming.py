from os import path 
import numpy as np
import scipy.io
import acoular 
import sys
import matplotlib.image as mpimg
from PIL import Image
from math import log, ceil, sqrt
from pylab import figure, plot, axis, imshow, colorbar, show, draw, title, tight_layout
from matplotlib import pyplot as plt

def coreBeamForm(micgeofile, datafile, imagefile, center_freq, inv_bandwidth, lower_freq, higher_freq, z_dist, userThresh=2):
	
	#print("Freq range: %.3f Hz - %.3f Hz" % (lower_freq, higher_freq))
	#print("Center: %.3f Hz || n: %.3f" % (center_freq, inv_bandwidth))

	#ts = acoular.TimeSamples(name=datafile)
	ts = acoular.MaskedTimeSamples(name=datafile)

	# Calibration factors (in Pa/V)
	# assuming input data is in V, this will convert data to Pa, and scale it according to calibration
	ts.calib = acoular.Calib(from_file="../xml/ECM8000_07_09_19_01.xml") # NEW 
	#invalid = [5,6,7,8]
	#invalid = [3,4, 7,8, 11,12, 15,16] # list of invalid channels (unwanted microphones etc.)
	invalid = []
	#ts.start = 179199
	
	ts.invalid_channels = invalid 

	ps = acoular.PowerSpectra(time_data=ts, block_size=1024 , window='Hanning')

	# Load and crop camera image
	im = Image.open(imagefile)
	width, height = im.size   # Get dimensions 
	new_width = 720
	new_height = 720#303  
	left = (width - new_width)/2
	top = (height - new_height)/2
	right = (width + new_width)/2
	bottom = (height + new_height)/2
	im = im.crop((left, top, right, bottom)) # Crop the center of the image
	px2cm = 3780.2717 
	dims = [new_width/px2cm, new_height/px2cm] # cropped picture size in meters 

	rg = acoular.RectGrid(x_min=-dims[0], x_max=dims[0], y_min=-dims[1], y_max=dims[1], z=z_dist,
                      increment=0.01)

	#rg = acoular.RectGrid(x_min=-0.2, x_max=0.2, y_min=-0.2, y_max=0.2, z=z_dist,
	#                     increment=0.01) 

	mg = acoular.MicGeom(from_file=micgeofile)
	mg.invalid_channels = invalid

	env = acoular.Environment(c = 346.04)
	st = acoular.SteeringVector( grid = rg, mics=mg, env=env) # sound propagation model
 
	bb = acoular.BeamformerBase(freq_data=ps, steer=st)
	#bb = acoular.fbeamform.BeamformerFunctional(freq_data=ps, steer=st, gamma=20, cached=True) 
	pm = bb.synthetic(center_freq, inv_bandwidth) # query for a desired center frequency, over an n-octave wide band

	Lm = acoular.L_p(pm) # convert to decibels 

	# load camera image to plot it 
	imshow(im, extent=rg.extend())
	plt.xlabel('[m]')
	plt.ylabel('[m]', rotation=0)
	plt.grid(True, alpha=0.2)

	# Calculated min/max sound pressure levels
	maxSPL = Lm.max()
	minSPL = Lm.min() 

	# save acoustic map results in .mat for post processing
	#TODO include experiment name in file name
	#scipy.io.savemat("../postProc/acMap.mat", mdict={'rg':rg, 'spl': Lm.T})

	minMapValue = maxSPL-userThresh 
	# plot intensities
	imshow(Lm.T, origin='lower', vmin=minMapValue, vmax=maxSPL, extent=rg.extend(),
				interpolation='bicubic', alpha=0.5, cmap='nipy_spectral') 

	# colorbar formatting 
	colorbarTicks = np.linspace(minMapValue, maxSPL, 6, endpoint=True)
	cbar = colorbar(ticks=colorbarTicks)  
	cbar.solids.set_edgecolor("face") 
	cbar.ax.set_ylabel('SPL [db]', rotation=0)  

	#title('Frequency range: {lf} - {hf} Hz\n\n(1/{band} Octave Band - Center: {fn} Hz)\n'.format(lf=lower_freq, hf=higher_freq, fn=center_freq, band=inv_bandwidth)); 
	title('Frequency range: {lf} - {hf} Hz\n\nDistance: {z} m'.format(lf=lower_freq, hf=higher_freq, z=z_dist))
	plt.tight_layout()
	#plt.tight_layout(pad=2.5, w_pad=2.5, h_pad=2.5)
	#figManager = plt.get_current_fig_manager()
	#figManager.window.showMaximized() 
	
	#plot(mg.mpos[0],mg.mpos[1],'o')
	#axis('equal')

	draw() 

def doBeamformingCenterFreq(args):  
	micgeofile = args[0]
	datafile = args[1]
	imagefile = args[2]
	center_freq = args[3]
	inv_bandwidth = args[4]  # actual bandwidth = 1/inv_bandwidth [octave]
	z_dist = args[5]
	
	lower_freq = round( center_freq / (2**(1/(2*inv_bandwidth))), 2)
	higher_freq = round( center_freq * (2**(1/(2*inv_bandwidth))), 2)

	coreBeamForm(micgeofile, datafile, imagefile, center_freq, inv_bandwidth, lower_freq, higher_freq, z_dist)


def doBeamformingGivenFreqs(args):  
	micgeofile = args[0]
	datafile = args[1]
	imagefile = args[2]
	lower_freq = float(args[3])# freq range start
	higher_freq = float(args[4]) # freq range end
	z_dist = float(args[5])
	userThresh = float(args[6])

	center_freq = sqrt(lower_freq*higher_freq)
	inv_bandwidth =  1/(2*log((center_freq/lower_freq), 2.0)) # actual bandwidth = 1/inv_bandwidth [octave]

	coreBeamForm(micgeofile, datafile, imagefile, center_freq, inv_bandwidth, lower_freq, higher_freq, z_dist, userThresh)
 