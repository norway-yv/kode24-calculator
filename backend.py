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
title = data["Har du en av disse begrepene i stillingstittelen din? "]
wage = data["Hva er din grunnlønn? (årslønn før skatt, uten eventuelle bonuser eller overtidsbetaling)"]
#Make data into list
age , county, workSituation, businessType, yearsEducation, workExperience, title, wage = age.tolist(), county.tolist(), workSituation.tolist(), businessType.tolist(), yearsEducation.tolist(), workExperience.tolist(), title.tolist(), wage.tolist()

#Create dictionaries for search
    #Age categories with lists of ages
ageCategories = {
    "20-24 år": [*range(20, 25)],
    "25-29 år": [*range(25, 30)],
    "30-34 år": [*range(30, 35)],
    "35-39 år": [*range(35, 40)],
    "40-44 år": [*range(40, 45)],
    "45-50 år": [*range(45, 51)],
    "50+ år": [*range(50, 100)],
    }
    #Create individual data strings for respondents
respondents = {}
for i in range(len(age)):
    toAdd = {i:{}}
    respondents.update(toAdd)
    toAdd = {"Age":age[i], "County":county[i], "Work Situation":workSituation[i], "Business Type":businessType[i], "Years Education":yearsEducation[i], "Work Experience":workExperience[i], "Title":title, "Wage":wage[i]}
    respondents[i].update(toAdd)
#Create list of options
def listOfOptions(parameter):
    parameters = []
    for occurence in parameter:
        if occurence not in parameters and occurence != "ikke oppgitt" and occurence != "vet ikke":
                parameters.append(occurence)
    return parameters
    
counties = listOfOptions(county)
workSituations = listOfOptions(workSituation)
businessTypes = listOfOptions(businessType)
yearsEducations = listOfOptions(yearsEducation)
workExperiences = listOfOptions(workExperience)
titles = listOfOptions(title)

inputs = np.loadtxt("database.txt", skiprows=1, usecols=1, dtype=str)
age_input = inputs[0]
county_input = inputs[1]
workSituation_input = inputs[2]
businessType_input = inputs[3]
yearsEducation_input = inputs[4]
workExperience_input = inputs[5]
title_input = inputs[6]

