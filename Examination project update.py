
print("\nEXAMINATION RESULTS")

math = int(input("Enter marks for Mathematics: "))
if math <0:
    print("You are not able to write a number less than 0.")
    math = int(input("Enter marks for Mathematics: "))

if math >100:
    print("You are not able to write a number greater than 100 .")
    math = int(input("Enter marks for Mathematics: "))
# english
english = int(input("Enter marks for English: "))
if english <0:
    print("You are not able to write a number less than 0.")
    english = int(input("Enter marks for English: ")) 

if english >100:
    print("You are not able to write a number greater than 100.")
    english = int(input("Enter marks for English: "))

# science
science = int(input("Enter marks for Science: "))  
if science <0:
    print("You are not able to write a number less than 0.")
    science = int(input("Enter marks for Science: "))    

if science >100:
    print("You are not able to write a number greater than 100 .")
    science = int(input("Enter marks for Science: "))  

average = (math + english + science) /3

if average>= 70 and average<= 100: 
    print("\n Grade A - You Exceeded expectations.")
elif average >= 50 and average <= 70:
    print("\nGrade B -You are Meeting expectations.")
elif average >= 20 and average<= 40:
    print("\nGrade C -You are Average in expectations.")
elif average >= 0 and average<= 30:
    print("\nGrade E -You failed.")

print("You got", round(average), "%")


