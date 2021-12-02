#Get input
age_input = int(round(float(input("Age: ")), 0))
county_input = input("County: ")
workSituation_input = input("Work situation: ")
businessType_input = input("Business type: ")
yearsEducation_input = input("Years education: ")
workExperience_input = input("Work experience: ")
title_input = input("Title: ")

#Delete content of database.txt
f = open('database.txt', 'r+')
f.truncate(0)

with open("database.txt", "a") as f:
    f.write("Name\tValue")
    f.write(f"county_input\t{county_input}")
    f.write(f"workSituation_input\t{workSituation_input}")
    f.write(f"businessType_input\t{businessType_input}")
    f.write(f"yearsEducation_input\t{yearsEducation_input}")
    f.write(f"workExperience_input\t{workExperience_input}")
    f.write(f"title_input\t{title_input}"))
