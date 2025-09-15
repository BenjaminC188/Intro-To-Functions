#strings represent characters or text

#bill = 3.14

students = ["Cadee", "Mason", "Andy"]

#Can reference each item in a list by their index
print(students[0]) #Prints Cadee

#add student
students.append("Alina")

#we can iterate or loop through a list
for student in students:
    print(student)

#Boolen true or false
# x = True
    y = False
#evaluations use double ==
if y == True:
    print("Hello Rodney")
else:
    print("Goodbye Rodney")

#Evaluations in Lists
x = 10
if x <10:
    print("Less")
elif x == 10:
    print("Equal")
else:
    print("Greter than 10")

students = ["Cadee", "Mason", "Andy", "Alina"]
for students in students:
    found = False
    if student == "Mason":
        print("Found Mason")
        found = True

name= "C a dee"
#print(name[0])
for letter in name:
    print(letter)
