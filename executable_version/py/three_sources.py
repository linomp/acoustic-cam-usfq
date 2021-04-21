# -*- coding: utf-8 -*-
# pylint: disable-msg=E0611, E1101, C0103, R0901, R0902, R0903, R0904, W0232
# ------------------------------------------------------------------------------
# Copyright (c) 2007-2017, Acoular Development Team.
# ------------------------------------------------------------------------------
"""Generates a test data set for three sources.
 
The simulation generates the sound pressure at 64 microphones that are
arrangend in the 'array64' geometry which is part of the package. The sound
pressure signals are sampled at 51200 Hz for a duration of 1 second.

Source location (relative to array center) and levels:

====== =============== ======
Source Location        Level 
====== =============== ======
1      (-0.1,-0.1,0.3) 1 Pa
2      (0.15,0,0.3)    0.7 Pa 
3      (0,0.1,0.3)     0.5 Pa
====== =============== ======
"""
import sys
from os import path
from acoular import __file__ as bpath, td_dir, MicGeom, WNoiseGenerator, PointSource, Mixer, WriteH5

if len(sys.argv) > 1:
    channels = int(sys.argv[1])
else:
    channels = 16

print(channels)

sfreq = 51200
duration = 1
nsamples = duration*sfreq

'''
if channels == 64:
    micgeofile = path.join(path.split(bpath)[0], 'xml', 'array_64.xml')
    h5savefile = '../data/examples/64_mics_samples.h5'
elif channels == 16:
    micgeofile = '../data/xml/16_mics_geom.xml'
    h5savefile = '../data/examples/16_mics_samples_2.h5'
elif channels == 30:
    micgeofile = '../data/xml/30_mics_geom.xml'
    h5savefile = '../data/examples/30_mics_samples.h5'
'''

micgeofile = '../data/xml/uma16.xml'
h5savefile = '../data/examples/3s_uma_16.h5'

m = MicGeom(from_file=micgeofile)
n1 = WNoiseGenerator(sample_freq=sfreq, numsamples=nsamples, seed=1)
n2 = WNoiseGenerator(sample_freq=sfreq, numsamples=nsamples, seed=2, rms=0.7)
n3 = WNoiseGenerator(sample_freq=sfreq, numsamples=nsamples, seed=3, rms=0.5)
p1 = PointSource(signal=n1, mpos=m,  loc=(-0.1, -0.1, 0.3))
p2 = PointSource(signal=n2, mpos=m,  loc=(0.1, 0, 0.3))
p3 = PointSource(signal=n3, mpos=m,  loc=(0, 0.1, 0.3))
p = Mixer(source=p1, sources=[p2, p3])
wh5 = WriteH5(source=p, name=h5savefile)
wh5.save()
