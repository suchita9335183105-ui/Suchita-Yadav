#Program By: Suchita Yadav
#Roll no.73
#List Assingement No:9

#Write a program that takes a list of names and a "search_name" from the user. print the index where the found.or "Not found"

names = ["Aman","Riya","Neha","Rahul"]
name = input("Enter name:")
if name in names:
    print ("index:", names.index(name))
else:
    print("Not found")