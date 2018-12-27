from collections import Counter
import re
import csv
from pandas import Series
from matplotlib import pyplot

series = Series.from_csv('vikingu_loto.csv', header = 0)
print(series.head())
series.plot()
pyplot.show()
