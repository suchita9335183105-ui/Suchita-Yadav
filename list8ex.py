#Program By: Suchita Yadav
#Roll no.73
#List Assingement No:8

#Given a list of numbers 1-20. create a new list that contain only the even numbers.

even = []
for i in range(1,21):
    if i%2==0:
        even.append(i)
print(even)