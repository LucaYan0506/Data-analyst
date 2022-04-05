import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://github.com/ine-rmotr-curriculum/FreeCodeCamp-Pandas-Real-Life-Example/blob/master/data/sales_data.csv"

sales = pd.read_csv(url,on_bad_lines='skip')