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

age , county, workSituation, businessType, yearsEducation, workExperience = age.tolist(), county.tolist(), workSituation.tolist(), businessType.tolist(), yearsEducation.tolist(), workExperience.tolist()
age2, county2, workSituation2, businessType2, yearsEducation2, workExperience2 = age, county, workSituation, businessType, yearsEducation, workExperience

"""
for i in range(len(age)-1):
    age2.remove(age[i])
    age2.append(age[i][:-2])
    county2.remove(county[i])
    county2.append(county[i])
    workSituation2.remove(workSituation[i])
    workSituation2.append(workSituation[i])
    businessType2.remove(businessType[i])
    businessType2.append(businessType[i])
    yearsEducation2.remove(yearsEducation[i])
    yearsEducation2.append(yearsEducation[i])
    workExperience2.remove(workExperience[i])
    workExperience2.append(workExperience[i])
print(age2)
"""
ageCategories = {
    "20-24": range(20, 24).tolist()
    "25-29": range(25, 29).tolist()
    "30-34": range(30, 34).tolist()
    "35-39": range(35, 39).tolist()
    "40-44": range(40, 44).tolist()
    "45-50": range(45, 50).tolist()
}
