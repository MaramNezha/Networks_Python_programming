#Defining the list
graduated_students = ['Maram', 'Sara','Ali','Ziad','Saleem']
#ask the user to enter a student name
name = input("Enter student name: ")
#check whether the name is graduated or not
if name in graduated_students:
    print(name,"is graduated")
else:
    print(name,"isn't graduated")