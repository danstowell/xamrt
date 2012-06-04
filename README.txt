---------------------------------------------------------
Xamrt - cross-associative tree regression algorithm
(c) 2009, 2010 Dan Stowell
All rights reserved.
---------------------------------------------------------


ABOUT

Xamrt is a multivariate regression-tree which can learn to associate regions of
two unlabelled distributions defined on the same axes.

Its theoretical background is described in a submitted research paper, and in
the author's PhD thesis:

@phdthesis{Stowell:2010,
	Author = {Stowell, D.},
	Title = {Musical expression through real-time voice timbre analysis: machine learning and timbral control},
	School = {School of Electronic Engineering and Computer Science, Queen Mary University of London},
	Url = {http://www.mcld.co.uk/thesis/},
	Year = {2010}}



INSTALLATION

The class file "Xamrt.py" is all you need, so you can copy/move it into a path
which your Python program searches. Alternatively put the whole folder in there.

The code is tested with Python 2.5.5 and numpy 1.3/1.4, provided by macports.



USAGE

The file defines a Python class called Xamrt. You initialise by creating an 
instance of the class fed with two arrays-of-arrays containing numerical data:

    from Xamrt import Xamrt
    p = Xamrt(a, b)

There's also a helpful utility function Xamrt.processcsv(path0, path1) which
applies the analysis to two CSV datafiles and writes out some datafiles with
the results.

For more detailed examples look in the "examples" folder which comes with the
download.

NOTE: If you want to use the plotting functions then you need to have GNUplot 
installed on your computer. By default the class expects the GNUplot executable
to be found at /opt/local/bin/gnuplot but you can modify that by setting the 
variable "Xamrt.gnuplotpath".

On Mac, you might need to run the scripts from within the X11 application (not
from Terminal.app) in order to get the plots easily. For example, to run the 
formantmap example I launch an X11 terminal, "cd" to this folder, then run

  PYTHONPATH=`pwd` python examples/formantmap.py 


The formantmap example includes vowel-formant data reproduced, with permission, 
from this paper:

  Hawkins, S. and Midgley, J. (2005). Formant frequencies of RP monophthongs 
      in four age groups of speakers. Journal of the International Phonetic 
      Association, 35(02):183Ð199. DOI: 10.1017/S0025100305002124



COPYRIGHTS

    Xamrt is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Xamrt is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with kdpee.  If not, see <http://www.gnu.org/licenses/>.
