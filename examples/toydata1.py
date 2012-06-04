#!/opt/local/bin/python

# Script generates two toy distributions in 3D (a cube and a hollow torus), 
# then runs XAMRT on them, plots, writes results to disk.
# Note that you'll need to be set up with GNUplot in the expected place to see the plots.

# Here's one way to invoke the script from a command line:
# PYTHONPATH=`pwd` python examples/toydata1.py

# Number of data points to generate in each
n = 1000

from numpy import *
a = (random.rand(n,3) * 2 + 2).round(2)
bpre = random.rand(n, 2) * pi * 2
b = array(map(lambda x: [cos(x[0]) * (cos(x[1])*0.5+1), sin(x[0]) * \
			(cos(x[1])*0.5+1), sin(x[1]) * 0.5], bpre)).round(2) + 5

from Xamrt import Xamrt
p = Xamrt(a, b, 3, maxdepth=12)
p.validate(a,b)

p.scatter()
p.vecmap(9, False)
p.vecmap()

p.write('./toydata1_output')
