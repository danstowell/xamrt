#!/opt/local/bin/python

# Like toydata1, but generates planar data in the shape of non-matching Ls:

# Number of data points to generate in each
n = 1000

from numpy import *
apre = random.rand(n,3)
for index, row in enumerate(apre):
	if row[0] < 0.5 and row[1] < 0.5:
		apre[index] = apre[index-1]

a = (apre * [2,2,0] + 2).round(2)
bpre = random.rand(n,3)
for index, row in enumerate(bpre):
	if row[0] > 0.5 and row[1] > 0.5:
		bpre[index] = bpre[index-1]

b = (bpre * [2,2,0] + 2).round(2)


from Xamrt import Xamrt
p = Xamrt(a, b, 3, maxdepth=8)
p.vecmap(Inf, False)
p.scatter(Inf, False)
p.scatter()
p.write('./toydata2_output')
