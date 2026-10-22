#NAME : DEVENDRA ODEDARA
#ENO: 92600584011

#Develop any Rule based system for an application of your choice.
print("==============================")
print(" CAREER GUIDANCE SYSTEM ")
print("==============================")
print("Answer the following questions with yes or no.")
print("\n")

q1 = str(input("Do you like coding ? ")).lower()
q2 = str(input("Do you like mathematics ? ")).lower()
q3 = str(input("Do you like biology ? ")).lower()
q4 = str(input("Do you like drawing ? ")).lower()
print("\n")
print("===== Career Suggestion =====")
print("Suggested Career: ",end="")
if q1 == "no" and q2 == "no" and q3 == "no" and q4 == "no":
    print("Explore your interests career options further.")
elif q1 == "no" and q2 == "no" and q3 == "no" and q4 == "yes":
    print("Graphic Designer/Animator")
elif q1 == "no" and q2 == "no" and q3 == "yes" and q4 == "no":
    print("Pharmacist/Nurse")
elif q1 == "no" and q2 == "no" and q3 == "yes" and q4 == "yes":
    print("Medical illustrator/Healthcare Educator")
elif q1 == "no" and q2 == "yes" and q3 == "no" and q4 == "no":
    print("Engineer/Data Analyst")
elif q1 == "no" and q2 == "yes" and q3 == "no" and q4 == "yes":
    print("Architect")
elif q1 == "no" and q2 == "yes" and q3 == "yes" and q4 == "no":
    print("Doctor")
elif q1 == "no" and q2 == "yes" and q3 == "yes" and q4 == "yes":
    print("Medical illustrator/Biomedical Designer")
elif q1 == "yes" and q2 == "no" and q3 == "no" and q4 == "no":
    print("Programmer/web Developer")
elif q1 == "yes" and q2 == "no" and q3 == "no" and q4 == "yes":
    print("Web Designer/UI-UX Designer")
elif q1 == "yes" and q2 == "no" and q3 == "yes" and q4 == "no":
    print("Health App Developer")
elif q1 == "yes" and q2 == "no" and q3 == "yes" and q4 == "yes":
    print("Medical illustrator")
elif q1 == "yes" and q2 == "yes" and q3 == "no" and q4 == "no":
    print("Software Engineer/computer Scientist")
elif q1 == "yes" and q2 == "yes" and q3 == "no" and q4 == "yes":
    print("Game Developer /UI Engineer")
elif q1 == "yes" and q2 == "yes" and q3 == "yes" and q4 == "no":
    print("Bioinformatics Scientist")
else:
    print("Biomedical Software Engineer/Medical Technology Specialist")

print("\n")
print("Thank you for using the Career Guidance Expert System!")
