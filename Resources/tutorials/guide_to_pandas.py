import pandas as pd
import numpy as np
from datetime import date, time
from datetime import datetime

# Set some Pandas options
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 25)


from sklearn import datasets



now = datetime.now()

now.day




time(3, 24)

date(1970, 9, 3)

age = now - datetime(1970, 9, 2)


vessels = pd.read_csv("../../data/AIS/vessel_information.csv", index_col='mmsi')
