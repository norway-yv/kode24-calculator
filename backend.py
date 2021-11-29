import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Get all data
data = pd.read_csv("data.csv", sep=",")
age = data["Hva er din alder?"]
county = data["I hvilket fylke ligger jobben din?"]

plt.plot(age, county)
plt.show()
