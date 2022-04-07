import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#clear console terminator   
import os
clear = lambda: os.system('cls')
clear()

url = "https://github.com/LucaYan0506/Data-analyst/raw/master/Lesson%201/data/sales_data.csv"

sales = pd.read_csv(url,parse_dates=['Date'])