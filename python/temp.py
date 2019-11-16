from pymodels import *
from trainData import *

r = Regression(return_xlabels("python/trialdata.csv",
                              ["SAT"]), return_ylabels("python/trialdata.csv", "GPA"))

r.fit_linear_regression()
