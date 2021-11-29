import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Get all data
data = pd.read_csv("data.csv", sep=",")
age = data["Hva er din alder?"]
county = data["I hvilket fylke ligger jobben din?"]
workSituation = data["Hva beskriver best din arbeidssituasjon?"]
businessType = data["Er du ansatt i det offentlige eller private næringsliv?"]
yearsEducation = data["Hvor mange års relevant, formell utdannelse har du?"]
workExperience = data["Hvor mange års relevant arbeidserfaring har du?"]
wage = data["Hva er din grunnlønn? (årslønn før skatt, uten eventuelle bonuser eller overtidsbetaling)"]
