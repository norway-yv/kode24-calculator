#Get input
age_input = int(round(float(input("Age: ")), 0))
county_input = input("County: ")
workSituation_input = input("Work situation: ")
businessType_input = input("Business type: ")
yearsEducation_input = int(round(float(input("Years education: ")), 0))
workExperience_input = int(round(float(input("Work experience: ")), 0))
title_input = input("Title: ")

#Delete content of database.txt
f = open('database.txt', 'r+')
f.truncate(0)

with open("database.txt", "a") as f:
    f.write("Name\tValue\n")
    f.write(f"county_input\t{county_input}\n")
    f.write(f"workSituation_input\t{workSituation_input}\n")
    f.write(f"businessType_input\t{businessType_input}\n")
    f.write(f"yearsEducation_input\t{yearsEducation_input}\n")
    f.write(f"workExperience_input\t{workExperience_input}\n")
    f.write(f"title_input\t{title_input}\n")
