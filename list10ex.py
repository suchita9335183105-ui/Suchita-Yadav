#Roll no.73
#List Assingement No:10
 
#Given a list of 10 Student marks.count how many students scored above 40.

marks = [35, 55, 60, 20, 90, 42, 38, 70, 80, 33]
count = 0
for m in marks:
    if m>40:
        count +=1
print("Students scored above 40:",count)