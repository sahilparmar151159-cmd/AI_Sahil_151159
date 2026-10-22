#NAME : DEVENDRA ODEDARA
#ENO: 92600584011

print("===== Expert System =====")
print("Answer the following questions with yes or no.")

q1 = str(input("Do you have fever?   : "))
q2 = str(input("Do you have cough?   : "))
q3 = str(input("Do you have headache?: "))

if(q1 == "no" and q2 == "no" and q3 == "no"):
    print("You seem to be healthy.")
elif(q1 == "yes" and q2 == "no" and  q3 == "no"):
    print("You may have a Mild Infection.")
elif(q1 == "no" and q2 == "yes" and  q3 == "no"):
    print("You may have a Throat Infection or Mild Cold")
elif(q1 == "no" and q2 == "no" and  q3 == "yes"):
    print("You may have Stress,Migraine,or Fatigue.")
elif(q1 == "yes" and q2 == "yes" and  q3 == "no"):
    print("You may have Flu.")
elif(q1 == "yes" and q2 == "no" and  q3 == "yes"):
    print("You may have Viral Fever.")
elif(q1 == "no" and q2 == "yes" and  q3 == "yes"):
    print("You may have Common Cold.")
else:
    print("You may have Flu or a Viral Infection.")
