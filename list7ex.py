#Program By: Suchita Yadav
#Roll no.73
#List Assingement No:7

#Ask a user for a fruit name . Check if it exists in your fruit_basket list using the in keyword.

fruits = ["apple","banana","mango","grapes"]
user = input("Enter fruit:")
if user in fruits:
    print("Fruit exists")
else:
    print("Fruit not found")