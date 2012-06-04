#!/opt/local/bin/python

# Analyses formant data from JIPA paper by Hawkins & Midgley (see README).

# Here's one way to invoke the script from a command line:
# PYTHONPATH=`pwd` python examples/formantmap.py

apath = "examples/formant_data/hm_grp1.csv"
bpath = "examples/formant_data/hm_grp4.csv"
from Xamrt import Xamrt
p = Xamrt.processcsv(apath, bpath, 2, maxdepth=12, plot=True, prune=0.9)

