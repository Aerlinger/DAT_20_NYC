import sys

# We'll be using these four modules *a lot*
import pandas as pd
import numpy as np
import sklearn
import matplotlib

import scipy
import bokeh
import statsmodels

# We'll be running IPython from the command line rather than within a script, but you'll want to make sure you have it installed
import IPython

# Information on the python version you're using along with how it was compiled:
print "Python installation:"
print sys.version

print "\nScientific python modules"
print "Pandas version: ", pd.__version__
print "Numpy version: ", np.__version__
print "Scikit learn version: ", sklearn.__version__
print "Matplotlib version: ", matplotlib.__version__

print "\nScipy version", scipy.__version__
print "Bokeh version: ", bokeh.__version__
print "Statsmodels version: ", statsmodels.__version__
print "IPython version: ", IPython.__version__

