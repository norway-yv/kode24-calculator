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
#Make data into list
age , county, workSituation, businessType, yearsEducation, workExperience = age.tolist(), county.tolist(), workSituation.tolist(), businessType.tolist(), yearsEducation.tolist(), workExperience.tolist()

#Create dictionaries for search
    #Age categories with lists of ages
ageCategories = {
    "20-24": [*range(20, 25)],
    "25-29": [*range(25, 30)],
    "30-34": [*range(30, 35)],
    "35-39": [*range(35, 40)],
    "40-44": [*range(40, 45)],
    "45-50": [*range(45, 51)],
    "50+": [*range(50, 100)],
    }
    #Create individual data strings for respondents
respondents = {}
for i in range(len(age)):
    toAdd = {i:{}}
    respondents.update(toAdd)
    toAdd = {"Age":age[i], "County":county[i], "Work Situation":workSituation[i], "Business Type":businessType[i], "Years Education":yearsEducation[i], "Work Experience":workExperience[i]}
    respondents[i].update(toAdd)
print(respondents)