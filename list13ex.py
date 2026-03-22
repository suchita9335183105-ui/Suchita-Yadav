#Program By: Suchita Yadav
#Roll no.73
#List Assingement No:13
 

ages = [10, 15, 20, 25, 17, 30]
minors =[]
adults =[]
for age in ages:
    if age < 18:
        minors.append(age)
    else:
        adults.append(age)
    print("Minors:",minors)
    print("adults:",adults)